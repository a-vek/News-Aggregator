# =============================================
from django.conf import settings
from django.conf.urls.static import static
# =============================================
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
# from news import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('notes/', include("notepad.urls")),
    path('', include("news.urls")),
    path('newsapi/', include('news.api.urls')),
    path('userapi/', include('users.userapi.urls')),
    path('register/', user_views.register, name='register'),
    path('category_list/', user_views.category_list, name='category_list'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
# path('cate/', user_views.cate, name='cate'),
# path('categorypicker/', user_views.categorypicker, name='categorypicker'),
# path('categorytracker/', user_views.categorytracker, name='categorytracker'),
# path('scrape/', views.scrape, name="scrape"),
# path('newslist/', views.news_list, name="home2"),

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
