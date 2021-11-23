from django.conf import settings
from django.db import models
from users.models import Category

# Create your models here.


class Headline(models.Model):
    # title = models.CharField(max_length=200)
    # url = models.TextField()
    # urlToImage = models.URLField(null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE)
    # user = models.ManyToManyField(Profile)
    # category1 = models.ForeignKey(
    #     Category, default=True, on_delete=models.CASCADE)
    #     # nid = models.CharField(max_length=150)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1800)
    url = models.URLField(null=True, blank=True)
    # category = models.CharField(max_length=120)
    # is_active = models.BooleanField(default=True)
#     language = models.CharField(max_length=100)
#     country = models.CharField(max_length=50)
#     # publishedAt = models.DateTimeField()
#     # category = models.CharField(Category, max_length=150)

    class Meta:
        verbose_name_plural = "News"
        # ordering = ('publishedAt')

    def __str__(self):
        return self.name


# class Headline(models.Model):
#     name = models.CharField(max_length=200)
#     desc = models.CharField(max_length=1800)
#     url = models.URLField(null=True, blank=True)
#     category = models.CharField(max_length=120)
#     language = models.CharField(max_length=100)
#     country = models.CharField(max_length=50)
#     user = models.ManyToManyField(Profile, blank=True)

#     class Meta:
#         verbose_name_plural = "News"

#     def __str__(self):
#         return self.name
# Scrape data coming from websites
# The posts will contain images, urls and titles

# model - headline(title, image, url)

# model - userprofile(user, last_scrape)

# cat_id = models.AutoField(primary_key=True)
# cat_name = models.CharField(max_length=1500)

# class Meta:
#     verbose_name_plural = "categories"

# def __str__(self):
#     return f'{self.cat_name}'
