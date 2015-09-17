from django.conf.urls import url
from scrum.views import ProductBacklogCreateView
from scrum.views import ProductBacklogDetailView
from scrum.views import ProductBacklogListView
from scrum.views import ProductBacklogUpdateView
from scrum.views import ProductBacklogDeleteView

from scrum.views import ReleaseBacklogCreateView
from scrum.views import ReleaseBacklogUpdateView
from scrum.views import ReleaseBacklogDeleteView
from scrum.views import ReleaseBacklogDetailView
from scrum.views import ReleaseBacklogListView

from scrum.views import home as scrum_home

urlpatterns = [
    url(
        r'product-backlog/update/(?P<pk>\d+)/$',
        ProductBacklogUpdateView.as_view(),
        name = "scrum_product_backlog_update"
    ),
    url(r'product-backlog/delete/(?P<pk>\d+)/$',
        ProductBacklogDeleteView.as_view(),
        name = "scrum_product_backlog_delete"
    ),
    url(
        r'product-backlog/detail/(?P<pk>\d+)/$',
        ProductBacklogDetailView.as_view(),
        name = "scrum_product_backlog_detail"
    ),
    url(
        r'product-backlog/create/$',
        ProductBacklogCreateView.as_view(),
        name = "scrum_product_backlog_create"
    ),
    url(
        r'product-backlog/$',
        ProductBacklogListView.as_view(),
        name = "scrum_product_backlog_list"
    ),
    # release_backlog
    url(
        r'release-backlog/update/(?P<pk>\d+)/$',
        ReleaseBacklogUpdateView.as_view(),
        name = "scrum_release_backlog_update"
    ),
    url(r'release-backlog/delete/(?P<pk>\d+)/$',
        ReleaseBacklogDeleteView.as_view(),
        name = "scrum_release_backlog_delete"
    ),
    url(
        r'release-backlog/detail/(?P<pk>\d+)/$',
        ReleaseBacklogDetailView.as_view(),
        name = "scrum_release_backlog_detail"
    ),
    url(
        r'release-backlog/create/$',
        ReleaseBacklogCreateView.as_view(),
        name = "scrum_release_backlog_create"
    ),
    url(
        r'release-backlog/$',
        ReleaseBacklogListView.as_view(),
        name = "scrum_release_backlog_list"
    ),
    url(
        r'product-backlog/$',
        ReleaseBacklogListView.as_view(),
        name = "scrum_release_backlog_list"
    ),
    url(
        r'$',
        scrum_home,
        name = "scrum_home"
    ),
]