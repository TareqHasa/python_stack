from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),
    path('shows', views.index),
    path('shows/new', views.show_new),
    path('shows/<int:id>', views.tv_shows),
    path('shows/<int:id>/edit', views.tv_shows_edit),
    path('shows/create', views.create_show),
    path('shows/<int:id>/update>', views.update_show),
    
]
