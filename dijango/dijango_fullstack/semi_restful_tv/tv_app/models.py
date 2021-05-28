from django.db import models


class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    released_date = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
