from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    code = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        help_text="Code defines the short and understandable word for role"
    )
    is_visible = models.BooleanField(default=True)
    icon_class = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "hris"