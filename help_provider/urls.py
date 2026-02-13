from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('post/<str:help_type>/', views.create_post, name='create_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post_selection/', views.post_selection, name='post_selection'),
    path('profile/', views.profile, name='profile'),
    path('my_posts/', views.my_posts, name='my_posts'),
]