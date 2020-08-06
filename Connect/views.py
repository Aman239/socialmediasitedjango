from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def Login(request):
    if request.user.is_authenticated:
        return redirect("UserProfile", request.user.username)

    form = AddUser_Form()
    error=False
    if request.method=="POST":
        un=request.POST["un"]
        ps=request.POST["ps"]
        usr=authenticate(username=un,password=ps)
        if usr!=None:
            login(request,usr)
            messages.success(request,"congrats! you have logged in successfully")
            return redirect("UserProfile",usr.username)
        error=True
    dict={"error":error,"form":form}
    return render(request,"login_register.html",dict)


def Logout(request):
    logout(request)
    return redirect("login")

def Register(request):
    if request.method=="POST":
        form=AddUser_Form(request.POST,request.FILES)
        if form.is_valid():
            data=form.save(commit=False)
            un=request.POST["un"]
            ps=request.POST["ps"]
            email=data.email

            usr=User.objects.create_user(un,email,ps)
            data.usr=usr
            data.save()
            return redirect("login")
    return HttpResponse("Register your self")


def UserProfile(request,Username):
    if not request.user.is_authenticated:
        return redirect("login")
    usr=User.objects.filter(username=Username)
    if not usr:
        logged_in_username=request.user.username
        return redirect("UserProfile",logged_in_username)
    connection=None
    if request.user.username != Username:
        user1=User.objects.get(username=Username)
        user2=User.objects.get(username=request.user.username)
        userdata1=UserDatabase.objects.get(usr=user1)
        userdata2=UserDatabase.objects.get(usr=user2)
        connection=connections.objects.filter(Q(sender=userdata1,reciever=userdata2)| Q(sender=userdata2,reciever=userdata1))
        if connection:
            connection = connection[0]
    usr=usr[0]
    User_Detail=UserDatabase.objects.get(usr=usr)


    blog_form=Blogs_Model_Form()
    all_posts=Blogs_Model.objects.filter(usr=usr).order_by("-date")


    like_by_me_ids=[]
    all_likes_by_me=Blog_likes.objects.filter(usr=request.user)
    for l in all_likes_by_me:
        like_by_me_ids.append(l.blog.id)


    comment_form = Comment_Blog_Form()

    ##### Comments Data ##############
    comments_data = Comment_Blogs.objects.all().order_by("-date")

    logged_in_user = request.user.username
    me_usr = User.objects.get(username=logged_in_user)
    me = UserDatabase.objects.get(usr=me_usr)
    connection = connections.objects.filter(Q(sender=me, status="friend") | Q(reciever=me, status="friend"))
    follower = ""
    User_Data = []
    for i in connection:
        UserData = UserDatabase.objects.get(id=i.sender.id)
        if UserData.id != me.id:
            User_Data.append(UserData)

        UserData = UserDatabase.objects.get(id=i.reciever.id)
        if UserData.id != me.id:
            User_Data.append(UserData)
    follower = User_Data
    print(len(User_Data))
    total_follower = len(User_Data)

    dict={"Profile":User_Detail,"connection":connection,"form":blog_form,"all_posts":all_posts,"like_by_me_ids":like_by_me_ids,
          "comment_form":comment_form,
        "comments_data":comments_data,
          "follower": follower,
          "total_follower": total_follower
          }
    return render(request,"user_details.html",dict)

def Update_user_detail(request,Username):
    if not request.user.is_authenticated:
        return redirect("login")
    logged_in_username = request.user.username
    if Username!=logged_in_username:
        return redirect("UserProfile",logged_in_username)
    usr = User.objects.filter(username=Username)
    usr=usr[0]
    User_Detail = UserDatabase.objects.get(usr=usr)
    form=Edit_User_Profile(request.POST or None,request.FILES or None,instance=User_Detail)
    if form.is_valid():
        form.save()
        return redirect("UserProfile", logged_in_username)
    dict = {"Profile": User_Detail,"form":form}
    return render(request, "update_user_detail.html", dict)



def All_Professionals(request,what):
    if not request.user.is_authenticated:
        return redirect("login")

    logged_in_user = User.objects.get(username=request.user.username)
    me=UserDatabase.objects.get(usr=logged_in_user)
    ##### count the connections
    Con_request = connections.objects.filter(reciever=me, status="Sent")
    Con_sent = connections.objects.filter(sender=me, status="Sent")
    Con_friend = connections.objects.filter(Q(sender=me, status="friend") | Q(reciever=me, status="friend")).order_by("-date")


    data=""
    if what=="all":
        data = UserDatabase.objects.all()
    if what == "Request":
        Connection = connections.objects.filter(reciever=me, status="Sent")
        User_Data=[]
        for c in Connection:
            ud=UserDatabase.objects.get(id=c.sender.id)
            User_Data.append(ud)
        data = User_Data
    if what == "Sent":
        Connection = connections.objects.filter(sender=me, status="Sent")
        User_Data = []
        for c in Connection:
            ud = UserDatabase.objects.get(id=c.reciever.id)
            User_Data.append(ud)
        data=User_Data
    if what == "friends":
        Connection = connections.objects.filter(Q(sender=me, status="friend") | Q(reciever=me, status="friend")).order_by("-date")
        Data = []
        for c in Connection:
            User_Data = UserDatabase.objects.get(Q(id=c.sender.id))
            if User_Data.id != me.id:
                Data.append(User_Data)
            User_Data = UserDatabase.objects.get(Q(id=c.reciever.id))
            if User_Data.id != me.id:
                Data.append(User_Data)
            data = Data
    dict={"data":data,"what":what,"Con_request":Con_request,"Con_sent":Con_sent,"Con_friend":Con_friend}
    return render(request,"professionals.html",dict)


def All_professionals_html(request,what):
    if not request.user.is_authenticated:
        return redirect("login")

    logged_in_user = User.objects.get(username=request.user.username)
    me=UserDatabase.objects.get(usr=logged_in_user)
    ##### count the connections
    Con_request = connections.objects.filter(reciever=me, status="Sent")
    Con_sent = connections.objects.filter(sender=me, status="Sent")
    Con_friend = connections.objects.filter(Q(sender=me, status="friend") | Q(reciever=me, status="friend")).order_by("-date")


    data=""
    if what=="all":
        data = UserDatabase.objects.all()
    dict = {
        "data": data,"me":me, "what": what, "Con_request": Con_request, "Con_sent": Con_sent, "Con_friend": Con_friend
         }
    return render(request, "professionals_html.html", dict)

def Manage_your_connection(request,action,u_id):
    if not request.user.is_authenticated:
        return redirect("login")
    if action == "Send_request":
        senderuser=User.objects.get(username=request.user.username)
        sender=UserDatabase.objects.get(usr=senderuser)
        reciever=UserDatabase.objects.get(id=u_id)
        connections.objects.create(sender=sender,reciever=reciever)
        return redirect("UserProfile", reciever.usr.username)
    if action == "Accept_request" or action == "Reject_request":
        recieveruser=User.objects.get(username=request.user.username)
        reciever=UserDatabase.objects.get(usr=recieveruser)
        sender=UserDatabase.objects.get(id=u_id)
        connection=connections.objects.filter(sender=sender,reciever=reciever)
        if connection:
            for c in connection:
                if action == "Accept_request":
                    c.status="friend"
                    c.save()
                if action == "Reject_request":
                    c.status="rejected"
                    c.save()
        return redirect("professionals","all")

    return HttpResponse("you want"+str(action)+"for user"+str(u_id))

def Add_Company(request):
    if not request.user.is_authenticated:
        return redirect("login")
    form=StartCompany_Form()
    if request.method == "POST":
        form=StartCompany_Form(request.POST,request.FILES)
        if form.is_valid():
            data=form.save(commit=False)
            Map = data.map_embed
            if 'width="600"' in Map:
                Map = Map.split('width="600"')
                Map.insert(1, 'width="100%"')
                Map = " ".join(Map)
                data.map_embed = Map

            data.usr=request.user
            data.save()
            return redirect("login")

    dict={"form":form}
    return render(request,"add_company.html",dict)

def CompanyDetails(request):
    if not request.user.is_authenticated:
        return redirect("login")
    usr=request.user
    company=Company_Model.objects.filter(usr=usr)
    if not company:
        return redirect("login")
    dict={
        "company":company
    }
    return render(request,"company_detail.html",dict)


def NewPost(request):
    if request.method=="POST":
        form=Blogs_Model_Form(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.usr=request.user
            data.save()
    return redirect("login")

def likebyme(request,b_id,Username):
     if not request.user.is_authenticated:
         return redirect("login")
     blog=Blogs_Model.objects.get(id=b_id)
     Blog_likes.objects.create(usr=request.user,blog=blog)
     return redirect("UserProfile",Username)

def Comments(request,b_id,Username):
    if not request.user.is_authenticated:
        return redirect("login")
    form=Comment_Blog_Form()
    print(form)
    if request.method=="POST":
        form=Comment_Blog_Form(request.POST,request.FILES)
        if form.is_valid():
            data=form.save(commit=False)
            data.usr=User.objects.get(username=Username)
            data.blog=Blogs_Model.objects.get(id=b_id)
            data.save()
            print("cheeje",data)
            return redirect("userProfile",Username)


    return render("userProfile",Username)

def See_Comments(request,b_id,Username):
    blog=Blogs_Model.objects.get(id=b_id)
    comments_data=Comment_Blogs.objects.filter(blog=blog)
    print("blog",blog)
    return redirect("userProfile",Username)