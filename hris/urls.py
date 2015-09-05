from django.conf.urls import include, url
from hris.views import home

urlpatterns = [
    url(r'$', home, name = "hris_home"),
]