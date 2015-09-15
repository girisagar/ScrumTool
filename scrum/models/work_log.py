from django.db import models
from hris.models import Employee
from scrum.models.user_story import UserStory

class WorkLog(models.Model):
    date = models.DateField(auto_now=True, auto_now_add=False)
    employee = models.ForeignKey(
        Employee, null=False,
        blank=False, related_name="worklog_employee"
    )
    user_story = models.ForeignKey(
        UserStory, null=False,
        blank=False, related_name="worklog_employee"
    )
    work_remaining = models.IntegerField(null=False, blank=False)
    work_done = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    # object CRUD related infomation
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(
        Employee, null=False,
        blank=False, related_name="worklog_created_by"
    )
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_by = models.ForeignKey(
        Employee, null=False,
        blank=False, related_name="worklog_updated_by"
    )
    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(
        auto_now=False, auto_now_add=False,
        null=True, blank=True
    )
    deleted_by = models.ForeignKey(
        Employee, null=True,
        blank=True, related_name="worklog_deleted_by"
    )

    class Meta:
        app_label = 'scrum'
        unique_together = ['date', 'employee']