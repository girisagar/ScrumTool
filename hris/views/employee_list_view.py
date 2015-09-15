from django.views.generic import ListView
from hris.models import Employee

class EmployeeListView(ListView):
    model = Employee
    queryset = Employee.objects.filter(is_deleted=False)
    paginate_by = 10