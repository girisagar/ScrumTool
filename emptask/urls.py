from django.conf.urls import url
from emptask.views import EmployeeTaskTemplateView
from emptask.views import DevelopmentTaskDetailView
from emptask.views import TestingTaskDetailView
from emptask.views import DevelopmentEstimateView
from emptask.views import TestEstimateView
from emptask.views import DevelopmentEstimateCreateView
from emptask.views import TestingEstimateCreateView
from emptask.views import TestingEstimateUpdateView
from emptask.views import DevelopmentEstimateUpdateView

urlpatterns = [
    url(r'test/detail/(?P<pk>\d+)/$',
        TestingTaskDetailView.as_view(),
        name="emptask_testing_task_detail"
    ),
    url(r'dev/detail/(?P<pk>\d+)/$',
        DevelopmentTaskDetailView.as_view(),
        name="emptask_development_task_detail"
    ),
    url(r'dev/estimate/(?P<pk>\d+)/$',
        DevelopmentEstimateView.as_view(),
        name="emptask_development_estimate"
    ),
    url(r'test/estimate/(?P<pk>\d+)/$',
        TestEstimateView.as_view(),
        name="emptask_testing_estimate"
    ),
    url(r'dev/daily-effort/create/(?P<story_id>\d+)/$',
        DevelopmentEstimateCreateView.as_view(),
        name="emptask_development_estimate_create"
    ),
    url(r'test/daily-effort/create/(?P<story_id>\d+)/$',
        TestingEstimateCreateView.as_view(),
        name="emptask_testing_estimate_create"
    ),
    url(r'test/daily-effort/update/(?P<pk>\d+)/$',
        TestingEstimateUpdateView.as_view(),
        name="emptask_testing_estimate_update"
    ),
    url(r'dev/daily-effort/update/(?P<pk>\d+)/$',
        DevelopmentEstimateUpdateView.as_view(),
        name="emptask_development_estimate_update"
    ),
    url(r'$',
        EmployeeTaskTemplateView.as_view(),
        name="emptask_mytask"
    ),
]