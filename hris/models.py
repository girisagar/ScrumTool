from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import os

class Employee(models.Model):
    user = models.OneToOneField(User, unique=True)
    image = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, "employee-image"))
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return self.user.email