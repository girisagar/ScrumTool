from django.views.generic.edit import CreateView
from hris.models import Employee
from hris.forms import EmployeeForm

class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm