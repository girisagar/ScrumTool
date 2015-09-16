from django.conf.urls import url
from hris.views import home
from hris.views import EmployeeCreateView
from hris.views import EmployeeDetailView
from hris.views import EmployeeListView
from hris.views import EmployeeUpdateView
from hris.views import EmployeeDeleteView

urlpatterns = [

    url(
        r'employee/update/(?P<pk>\d+)/$',
        EmployeeUpdateView.as_view(),
        name = "hris_employee_update"
    ),
    url(
        r'employee/delete/(?P<pk>\d+)/$',
        EmployeeDeleteView.as_view(),
        name = "hris_employee_delete"
    ),
    url(
        r'employee/detail/(?P<pk>\d+)/$',
        EmployeeDetailView.as_view(),
        name = "hris_employee_detail"
    ),
    url(
        r'employee/create/$',
        EmployeeCreateView.as_view(),
        name = "hris_employee_create"
    ),
    url(
        r'employee/$',
        EmployeeListView.as_view(),
        name = "hris_employee_list"
    ),
    url(
        r'$',
        home,
        name = "hris_home"
    ),
]