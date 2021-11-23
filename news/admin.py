from django.contrib import admin
from news.models import Headline

# Register your models here.

admin.site.register(Headline)


# class AdminHeadline(admin.ModelAdmin):
#     list_display = ('title', 'category')


# admin.site.register(Category)
