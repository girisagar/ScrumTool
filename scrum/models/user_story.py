from django.db import models
from scrum.models.product_backlog import ProductBacklog
from scrum.models.release_backlog import ReleaseBacklog
from scrum.models.sprint import Sprint
from hris.models import Employee

class UserStory(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=2000, blank=True, null=True)
    assiged_developer = models.ForeignKey(
        Employee, null=True,
        blank=True, related_name="userstory_assiged_developer"
    )
    developer_effort = models.IntegerField(null=True, blank=True)
    assiged_tester = models.ForeignKey(
        Employee, null=True,
        blank=True, related_name="userstory_assiged_tester"
    )
    tester_effort = models.IntegerField(null=True, blank=True)
    product_backlog = models.ForeignKey(ProductBacklog, null=True, blank=True)
    release_backlog = models.ForeignKey(ReleaseBacklog, null=True, blank=True)
    sprint = models.ForeignKey(Sprint, null=True, blank=True)

    # object CRUD related infomation
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(
        Employee, null=False,
        blank=False, related_name="userstory_created_by"
    )
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_by = models.ForeignKey(
        Employee, null=False,
        blank=False, related_name="userstory_updated_by"
    )
    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(
        auto_now=False, auto_now_add=False,
        null=True, blank=True
    )
    deleted_by = models.ForeignKey(
        Employee, null=True,
        blank=True, related_name="userstory_deleted_by"
    )

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'scrum'