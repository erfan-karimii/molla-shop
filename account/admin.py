from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

UserAdmin.fieldsets +=(
    ('فیلد های شخصی', {"fields": ("phone","token","is_verify",)}),
)


admin.site.register(MyUser, UserAdmin)