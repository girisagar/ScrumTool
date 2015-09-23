from django.db import models
from hris.models import Employee
from scrum.models import ReleaseBacklog

class Sprint(models.Model):
    name = models.CharField(
        max_length=50,
        null=False, blank=False,
        help_text = "Sprint name should be in order like Sprint-1, Sprint-2, and so on"
    )
    release_backlog = models.ForeignKey(
        ReleaseBacklog, null=False,
        blank=False
    )
    sprint_start = models.DateTimeField(
        auto_now=False, auto_now_add=False,
        null=True, blank=True
    )
    sprint_end = models.DateTimeField(
        auto_now=False, auto_now_add=False,
        null=True, blank=True
    )
    # object CRUD related infomation
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(
        Employee, null=False,
        blank=False, related_name="sprint_created_by"
    )
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_by = models.ForeignKey(
        Employee, null=False,
        blank=False, related_name="sprint_updated_by"
    )
    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(
        auto_now=False, auto_now_add=False,
        null=True, blank=True
    )
    deleted_by = models.ForeignKey(
        Employee, null=True,
        blank=True, related_name="sprint_deleted_by"
    )

    class Meta:
        app_label = 'scrum'

    def __unicode__(self):
        return self.name

    @property
    def product_backlog(self):
        return self.release_backlog.product_backlog
    