from django.db import models
from django.contrib.auth.models import User
from hris.models.role import Role

class Employee(models.Model):
    user = models.OneToOneField(
        User, null=False,
        blank=False, related_name="employee"
    )
    image = models.ImageField(
        upload_to="hris/employee-image",
        null=True, blank=True
    )
    emp_id = models.CharField(
        max_length=10, null=False,
        blank=False, unique=True
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    roles = models.ManyToManyField(Role)
    
    # object CRUD related infomation
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(
        'Employee', null=True,
        blank=True, related_name="employee_created_by"
    )
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_by = models.ForeignKey(
        'Employee', null=True,
        blank=True, related_name="employee_updated_by"
    )
    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(
        auto_now=False, auto_now_add=False,
        null=True, blank=True
    )
    deleted_by = models.ForeignKey(
        'Employee', null=True,
        blank=True, related_name="employee_deleted_by"
    )

    def __unicode__(self):
        return str(self.user.username)

    @property
    def address(self):
        return "{0}\n{1}, {2}, {3}".format(self.street, self.city, self.state, self.zip)

    @property
    def name(self):
        return self.user.get_full_name()

    class Meta:
        app_label = "hris"