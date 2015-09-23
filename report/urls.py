from django.conf.urls import url

# from report.views import SprintBurndownChartView
from report.views import BurnDownChartListView

urlpatterns = [
    url(r'^burndownchart/$', BurnDownChartListView.as_view(), name="burndownchart_home"),
    url(r'^burndownchart/(?P<pk>\d+)/$', "report.views.sprint_burndownchart.sprint", name="burndownchart"),    
]