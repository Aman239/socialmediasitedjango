from django import forms
from .models import *


class AddUser_Form(forms.ModelForm):
    class Meta:
        model=UserDatabase
        exclude=("usr","dob","location","degree","website","experience","company","profile_title","facebook_url","twitter_url","email_url","linkedin_url","instaram_url")
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control",}),
            "email":forms.EmailInput(attrs={"class":"form-control",}),
            "number":forms.NumberInput(attrs={"class":"form-control",}),
            "image":forms.FileInput(attrs={"class":"form-control", "onchange":"loadFile(event)"}),
            "about":forms.Textarea(attrs={"class":"form-control","rows":"5"}),
        }



class Edit_User_Profile(forms.ModelForm):
    class Meta:
        model=UserDatabase
        exclude=("usr",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", }),
            "email": forms.EmailInput(attrs={"class": "form-control", }),
            "number": forms.NumberInput(attrs={"class": "form-control", }),
            "about": forms.Textarea(attrs={"class": "form-control", "rows": "5"}),
            "dob": forms.DateInput(attrs={"class": "form-control", }),
            "degree": forms.TextInput(attrs={"class": "form-control", }),
            "location": forms.TextInput(attrs={"class": "form-control", }),
            "website": forms.TextInput(attrs={"class": "form-control", }),
            "experience": forms.TextInput(attrs={"class": "form-control", }),
            "company": forms.TextInput(attrs={"class": "form-control", }),
            "profile_title": forms.TextInput(attrs={"class": "form-control", }),
            "instaram_url":forms.URLInput(attrs={"class": "form-control", }),
            "facebook_url":forms.URLInput(attrs={"class": "form-control", }),
            "linkedin_url":forms.URLInput(attrs={"class": "form-control", }),
            "twitter_url":forms.URLInput(attrs={"class": "form-control", }),
            "email_url":forms.URLInput(attrs={"class": "form-control", }),


        }


class StartCompany_Form(forms.ModelForm):
    class Meta:
        model=Company_Model
        exclude=("usr",)
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control",}),
            "title":forms.TextInput(attrs={"class":"form-control",}),
            "website":forms.TextInput(attrs={"class":"form-control",}),
            "address":forms.TextInput(attrs={"class":"form-control",}),
            "email":forms.EmailInput(attrs={"class":"form-control",}),
            "number":forms.NumberInput(attrs={"class":"form-control",}),
            "logo":forms.FileInput(attrs={"class":"form-control", "onchange":"loadFile(event)"}),
            "map_embed":forms.Textarea(attrs={"class":"form-control",}),
            "mapurl":forms.URLInput(attrs={"class":"form-control",}),


        }

class Blogs_Model_Form(forms.ModelForm):
    class Meta:
        model=Blogs_Model
        exclude=("usr",)
        widgets={

            "title":forms.TextInput(attrs={"class":"form-control",}),
            "youtube_video":forms.TextInput(attrs={"class":"form-control",}),
            "blog":forms.Textarea(attrs={"class":"form-control",}),
            "image":forms.FileInput(attrs={"class":"form-control",}),

        }
class Comment_Blog_Form(forms.ModelForm):
    class Meta:
        model=Comment_Blogs
        exclude=("usr","blog",)
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", }),
            "date": forms.DateInput(attrs={"class": "form-control", }),
            "youtube_embad": forms.Textarea(attrs={"class": "form-control", }),
            "content": forms.Textarea(attrs={"class": "form-control", }),
            "image":forms.FileInput(attrs={"class": "form-control", }),
        }