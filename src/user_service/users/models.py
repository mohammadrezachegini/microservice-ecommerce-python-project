from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class USer(AbstractUser):
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        ordering = ['-created_at']