from django.conf.urls import url
from scrum.views import ProductBacklogCreateView
from scrum.views import ProductBacklogDetailView
from scrum.views import ProductBacklogListView
from scrum.views import ProductBacklogUpdateView
from scrum.views import ProductBacklogDeleteView
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
    # add urls here
    url(
        r'$',
        scrum_home,
        name = "scrum_home"
    ),
]