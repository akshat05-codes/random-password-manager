from django.db import models

# Create your models here.
class Note(models.Model):
    site = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site
class PasswordEntry(models.Model):
    site = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
