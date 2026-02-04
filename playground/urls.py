from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('google/', views.google_redirect),
    path('people/',views.home)
]
