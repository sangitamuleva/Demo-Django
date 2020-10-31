from django.urls import path 
from .views import *
from auth_user import views as auth_user_views
from django.contrib.auth import views as django_views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',login_required(post_list.as_view()),name='all_post'),
    path('post/create/',login_required(post_create.as_view()),name='create_post'),
    path('post/<pk>/',login_required(post_detail.as_view()),name='post_detail'),
    path('post/<pk>/update/',login_required(post_update.as_view()),name='post_update'),
    path('post/<pk>/delete/',login_required(post_delete.as_view()),name='post_delete'),
    path('user/register/',auth_user_views.register,name='register'),
    path('user/login/',django_views.LoginView.as_view(template_name='auth/login.html'),name='login'),
    path('user/logout/',login_required(django_views.LogoutView.as_view(template_name='auth/logout.html')),name='logout'),

    path('category/',category_list,name='all_category'),   
    path('category/create/',category_create,name='create_category'),
    path('category/<pk>/',category_detail,name='category_detail'),
    path('category/<pk>/update/',category_update,name='category_update'),
    path('category/<pk>/delete/',category_delete,name='category_delete'),

     path('subcategory/',subcategory_list,name='all_subcategory'),   
    path('subcategory/create/',subcategory_create,name='create_subcategory'),
    path('subcategory/<pk>/',subcategory_detail,name='subcategory_detail'),
    path('subcategory/<pk>/update/',subcategory_update,name='subcategory_update'),
    path('subcategory/<pk>/delete/',subcategory_delete,name='subcategory_delete'),
 

]