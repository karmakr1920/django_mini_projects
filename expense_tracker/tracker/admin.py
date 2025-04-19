from django.contrib import admin
from .models import CustomUser, Category, Expense
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Category)
admin.site.register(Expense)
