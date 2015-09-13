from django.conf.urls import include, url
from hris.views import home
from hris.views import EmployeeCreateView
from hris.views import EmployeeListView
from hris.views import EmployeeUpdateView

urlpatterns = [

    url(r'employee/update/(?P<pk>\d+)/$', EmployeeUpdateView.as_view(), name = "hris_employee_update"),
    url(r'employee/create/$', EmployeeCreateView.as_view(), name = "hris_employee_create"),
    url(r'employee/$', EmployeeListView.as_view(), name = "hris_employee_list"),
    url(r'$', home, name = "hris_home"),
]