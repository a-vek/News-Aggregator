from django.contrib import admin
# from .models import Category
from .models import Profile, Category


admin.site.register(Profile)
# admin.site.register(UserCategory)


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'image']
admin.site.register(Category)


# @admin.register(Category)
# class CategoriesAdmin(admin.ModelAdmin):
#     list_display = ['cat_name']
