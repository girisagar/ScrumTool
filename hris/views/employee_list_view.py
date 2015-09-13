from django.views.generic import ListView
from hris.models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    queryset = Employee.objects.all()
    paginate_by = 10