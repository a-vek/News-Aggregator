from django.urls import path
from news.views import scrape, news_list
from . import views

urlpatterns = [
    # path('', views.index, name="home"),
    # path('newslist', news_list, name="home"),
]
