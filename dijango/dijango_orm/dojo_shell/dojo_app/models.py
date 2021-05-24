from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Dojo (models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state= models.CharField(max_length=2)
    desc=models.TextField(default="old dojo")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Ninja(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dojo=models.ForeignKey(Dojo,related_name="ninja",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)