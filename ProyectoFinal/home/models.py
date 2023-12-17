from django.db import models
from django.utils import timezone
from django.conf import settings
from django import forms

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.CharField(max_length=9999)
    imageUrl = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True, blank=True)    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Update the timestamp when saving the model
        self.updated_at = timezone.now()
        if not self.created_at:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']