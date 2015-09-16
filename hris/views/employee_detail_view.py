from django.views.generic import DetailView
from hris.models import Employee

class EmployeeDetailView(DetailView):
    model = Employee