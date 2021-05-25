from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('adddojo',views.add_dojo),
    path('addninja',views.add_ninja)
]