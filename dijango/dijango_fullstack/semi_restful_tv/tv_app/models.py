from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Description should be at least 3 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    released_date = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()