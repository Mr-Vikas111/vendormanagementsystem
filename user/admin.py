from django.contrib import admin
from user.models import base as base_models
from django.contrib.auth.admin import UserAdmin



@admin.register(base_models.User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('password',)}),
        (('Personal info'), {'fields': ('email','is_staff', 'is_superuser')}),
        (('Permissions'), {'fields': ('permissions',)}),
        (('Important dates'), {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
       
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('name','email')
    list_display = ['id','name','email',]
    list_filter = ['date_joined',"is_staff"]
    list_display_links = ["id","name"]
    ordering = ('-id',)