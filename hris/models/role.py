from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    icon_class = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "hris"