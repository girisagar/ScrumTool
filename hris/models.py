from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import os

class Role(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    icon_class = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, "employee-image"), null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    roles = models.ManyToManyField(Role, null=True, blank=True)

    def __unicode__(self):
        return str(self.user.username)

    @property
    def address(self):
        return '{0}\n{1}, {2}, {3}'.format(self.street, self.city, self.state, self.zip)