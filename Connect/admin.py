from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserDatabase)
admin.site.register(connections)
admin.site.register(Company_Model)
admin.site.register(Blogs_Model)
admin.site.register(Blog_likes)
admin.site.register(Comment_Blogs)