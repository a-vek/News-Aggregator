from django.db import router
from django.urls import path, include
from rest_framework import urlpatterns
from news.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.HeadlineViewSet, basename='headline')

urlpatterns = [
    # path('', views.HeadlineViewSet, name='headline'),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
