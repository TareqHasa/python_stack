from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.root),
    path('blogs',views.index),
    path('blogs/new',views.new),
    path('blogs/create',views.creat),
    path('blogs/<int:number>',views.show),
    path('blogs/<int:number>/edit',views.edit),
    path('blogs/<int:number>/delete',views.destroy),
]