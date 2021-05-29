from django.contrib.messages.api import success
from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('regester',views.regester),
    path('success',views.success),
    path('logout',views.logout),
    path('login',views.login)
]