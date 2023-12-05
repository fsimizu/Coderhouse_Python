from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=9999)
    imageUrl = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True, blank=True)    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Update the timestamp when saving the model
        self.updated_at = timezone.now()
        if not self.created_at:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    