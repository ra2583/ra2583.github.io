from week10project import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('ccu410210041', views.ccu410210041_function)
]
