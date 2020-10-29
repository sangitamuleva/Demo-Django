from django.urls import path 
from .views import *
from auth_user import views as auth_user_views
from django.contrib.auth import views as django_views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',login_required(post_list.as_view()),name='all_post'),
    path('create/',login_required(post_create.as_view()),name='create_post'),
    path('<pk>/',login_required(post_detail.as_view()),name='post_detail'),
    path('<pk>/update/',login_required(post_update.as_view()),name='post_update'),
    path('<pk>/delete/',login_required(post_delete.as_view()),name='post_delete'),
    path('user/register/',auth_user_views.register,name='register'),
    path('user/login/',django_views.LoginView.as_view(template_name='auth/login.html'),name='login'),
    path('user/logout/',login_required(django_views.LogoutView.as_view(template_name='auth/logout.html')),name='logout')

]