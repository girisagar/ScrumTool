from django.db import models
from hris.models import Employee

class ReleaseBacklog(models.Model):
    name = models.CharField(
        max_length=50, unique=True,
        null=False, blank=False
    )
    scrum_master = models.ForeignKey(Employee, null=True, blank=True)

    # object CRUD related infomation
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(
        Employee, null=False,
        blank=False, related_name="release_backlog_created_by"
    )
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_by = models.ForeignKey(
        Employee, null=False,
        blank=False, related_name="release_backlog_updated_by"
    )
    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(
        auto_now=False, auto_now_add=False,
        null=True, blank=True
    )
    deleted_by = models.ForeignKey(
        Employee, null=True,
        blank=True, related_name="release_backlog_deleted_by"
    )

    class Meta:
        app_label = 'scrum'