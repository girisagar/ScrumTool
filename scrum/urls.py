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
from scrum.views import ReleaseBacklogStoryDeleteView
from scrum.views import ReleaseBacklogAssignScrumMasterView

from scrum.views import home as scrum_home

from scrum.views import UserStoryCreateView
from scrum.views import UserStoryDeleteView
from scrum.views import UserStoryDetailView
from scrum.views import UserStoryUpdateView
from scrum.views import UserStoryToReleaseView
from scrum.views import UserStoryToSprintView
from scrum.views import SprintStoryDeleteView

from scrum.views import SprintCreateView
from scrum.views import SprintDeleteView
from scrum.views import SprintUpdateView

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
        r'product-backlog/(?P<pk>\d+)/$',
        ProductBacklogDetailView.as_view(),
        name = "scrum_product_backlog"
    ),
    url(
        r'product-backlog/create/$',
        ProductBacklogCreateView.as_view(),
        name = "scrum_product_backlog_create"
    ),
    url(
        r'product-backlog/(?P<product_id>\d+)/move-stories/$',
        UserStoryToReleaseView.as_view(),
        name = "scrum_user_story_to_release"
    ),
    url(
        r'product-backlog/$',
        ProductBacklogListView.as_view(),
        name = "scrum_product_backlog_list"
    ),
    # release_backlog
    url(
        r'product-backlog/(?P<product_id>\d+)/release-backlog/update/(?P<pk>\d+)/$',
        ReleaseBacklogUpdateView.as_view(),
        name = "scrum_release_backlog_update"
    ),
    url(
        r'product-backlog/(?P<product_id>\d+)/release-backlog/delete/(?P<pk>\d+)/$',
        ReleaseBacklogDeleteView.as_view(),
        name = "scrum_release_backlog_delete"
    ),
    url(
        r'product-backlog/(?P<product_id>\d+)/release-backlog/create/$',
        ReleaseBacklogCreateView.as_view(),
        name = "scrum_release_backlog_create"
    ),
    url(
        r'release-backlog/detail/(?P<pk>\d+)/$',
        ReleaseBacklogDetailView.as_view(),
        name = "scrum_release_backlog_detail"
    ),
    url(
        r'release-backlog/assign-scrum-master/(?P<pk>\d+)/$',
        ReleaseBacklogAssignScrumMasterView.as_view(),
        name = "scrum_release_backlog_assign_scrum_master"
    ),
    url(
        r'release-backlog/user-story/delete/(?P<pk>\d+)/$',
        ReleaseBacklogStoryDeleteView.as_view(),
        name = "scrum_release_backlog_user_story_delete"
    ),
    url(
        r'release-backlog/$',
        ReleaseBacklogListView.as_view(),
        name = "scrum_release_backlog_list"
    ),
    url(
        r'product-backlog/(?P<product_id>\d+)/user-story/create/$',
        UserStoryCreateView.as_view(),
        name = "scrum_user_story_create"
    ),
    url(
        r'product-backlog/(?P<product_id>\d+)/user-story/delete/(?P<pk>\d+)/$',
        UserStoryDeleteView.as_view(),
        name = "scrum_user_story_delete"
    ),
    url(
        r'product-backlog/(?P<product_id>\d+)/user-story/detail/(?P<pk>\d+)/$',
        UserStoryDetailView.as_view(),
        name = "scrum_user_story_detail"
    ),
    url(
        r'product-backlog/(?P<product_id>\d+)/user-story/update/(?P<pk>\d+)/$',
        UserStoryUpdateView.as_view(),
        name = "scrum_user_story_update"
    ),
    url(
        r'release-backlog/(?P<release_id>\d+)/move-stories/$',
        UserStoryToSprintView.as_view(),
        name = "scrum_user_story_to_sprint"
    ),
    url(
        r'release-backlog/(?P<release_id>\d+)/sprint/create/$',
        SprintCreateView.as_view(),
        name = "scrum_sprint_create"
    ),
    url(
        r'sprint/delete/(?P<pk>\d+)/$',
        SprintDeleteView.as_view(),
        name = "scrum_sprint_delete"
    ),
    url(
        r'sprint/update/(?P<pk>\d+)/$',
        SprintUpdateView.as_view(),
        name = "scrum_sprint_update"
    ),
    url(
        r'sprint/user-story/delete/(?P<pk>\d+)/$',
        SprintStoryDeleteView.as_view(),
        name = "scrum_sprint_user_story_delete"
    ),
    # url(
    #     r'user-story/assign-developer/(?P<pk>\d+)/delete/$',
    #     SprintStoryDeleteView.as_view(),
    #     name = "scrum_sprint_user_story_delete"
    # ),
    url(
        r'$',
        scrum_home,
        name = "scrum_home"
    ),
]