from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField(max_length=255)
    email=models.TextField(max_length=255)
    age= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
