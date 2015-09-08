from django.conf.urls import include, url
from hris.views import home
from hris.views import EmployeeCreate

urlpatterns = [
    url(r'employee/create/$', EmployeeCreate.as_view(), name = "hris_employee_create"),
    # url(r'$', home, name = "hris_home"),
]