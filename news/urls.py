from django.urls import path
from news.views import scrape
from . import views

urlpatterns = [
    path('scrape/', views.scrape, name="scrape"),
    path('', views.news_list, name="home"),
    # path('articles/', views.news_list, name="home")
]
