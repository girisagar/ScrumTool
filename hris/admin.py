from django.contrib import admin
from hris.models import Employee
from hris.models import Role

admin.site.register(Employee)
admin.site.register(Role)