from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDatabase(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=150,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    about=models.TextField(null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    degree=models.CharField(max_length=100,null=True,blank=True)
    website=models.CharField(max_length=100,null=True,blank=True)
    experience=models.CharField(max_length=100,null=True,blank=True)
    company=models.CharField(max_length=100,null=True,blank=True)
    profile_title=models.CharField(max_length=100,null=True,blank=True)
    facebook_url=models.URLField(max_length=200,null=True,blank=True)
    twitter_url=models.URLField(max_length=200,null=True,blank=True)
    email_url=models.URLField(max_length=200,null=True,blank=True)
    linkedin_url=models.URLField(max_length=200,null=True,blank=True)
    instaram_url=models.URLField(max_length=200,null=True,blank=True)



    def __str__(self):
        return self.name


class connections(models.Model):
    sender=models.ForeignKey(UserDatabase,related_name="sender",on_delete=models.CASCADE,null=True,blank=True)
    reciever=models.ForeignKey(UserDatabase,related_name="reciever",on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=30,null=True,blank=True,default="Sent")
    date=models.DateField(auto_now_add=True,null=True)



class Company_Model(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    logo=models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    number = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    website = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    map_embed=models.TextField(null=True,blank=True)
    mapurl=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

class Blogs_Model(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    blog=models.TextField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    youtube_video=models.TextField(null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blog_likes(models.Model):
    usr=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    blog=models.ForeignKey(Blogs_Model,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.usr
class Comment_Blogs(models.Model):
    usr=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    blog = models.ForeignKey(Blogs_Model, on_delete=models.CASCADE, null=True, blank=True)
    content=models.TextField(null=True,blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    youtube_embad = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.usr.username