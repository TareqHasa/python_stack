from django.urls import path

from . import views

urlpatterns = [
    path('shows/', views.index),
    path('shows/new', views.show_new),
    path('shows/<int:id>', views.tv_shows),
    path('shows/<int:id>/edit', views.tv_shows_edit),
    path('create_show', views.create_show),
    path('update_show/<int:id>', views.update_show),
    path('delete/<int:id>', views.delete)


]
