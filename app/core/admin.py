from django.contrib import admin

# Register your models here.

""" Django admin customization """

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from core import  models


class UserAdmmin(BaseUserAdmin):
    ordering=['id']
    list_display=['email','name']
    
    
    
admin.site.reqister(models.User, UserAdmin)