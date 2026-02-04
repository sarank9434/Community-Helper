from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:help_type>/', views.create_post, name='create_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
]