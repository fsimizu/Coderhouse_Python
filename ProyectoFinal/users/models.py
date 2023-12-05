from django.db import models
from django.utils import timezone

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.RESTRICT)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    createdAt = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    