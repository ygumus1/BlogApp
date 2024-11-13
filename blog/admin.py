from django.contrib import admin
from .models import Post,Categories,Comment,UserProfile

# Register your models here.

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Categories)
admin.site.register(Comment)
