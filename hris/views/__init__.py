from django.shortcuts import render
from hris.views.employee_create_view import EmployeeCreateView 
from hris.views.employee_update_view import EmployeeUpdateView
from hris.views.employee_delete_view import EmployeeDeleteView
from hris.views.employee_list_view import EmployeeListView

def home(request):
    return render(request, "home.html", {})