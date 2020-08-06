"""SocialMedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Connect.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login,name="login"),
    path('Logout/',Logout,name="logout"),
    path('Register/',Register,name="register"),
    path('in/<str:Username>/',UserProfile,name="UserProfile"),
    path('in/Edit/<str:Username>/',Update_user_detail,name="UpdateUserProfile"),


    path('all_professionals/<str:what>/',All_Professionals,name="professionals"),
    path('professionals_html/<str:what>/',All_professionals_html,name="professionals_html"),
    path('connection/<str:action>/<int:u_id>/',Manage_your_connection,name="connections"),

     path('add_company/',Add_Company,name="addcompany"),
     path('your_companydetails/',CompanyDetails,name="companydetails"),
     path('post_new_blog/',NewPost,name="newpost"),
     path('connection/<int:b_id>/<str:Username>/',likebyme,name="likes"),
     path('comments/<int:b_id>/<str:Username>/',Comments,name="comments"),
    path('see_comments/<int:b_id>/<str:Username>/', See_Comments, name="see_comments"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
