from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from scrum.models import ProductBacklog
from scrum.services import ProductBacklogService
from scrum.services import ReleaseBacklogService
from scrum.services import UserStoryService

class ProductBacklogDetailView(DetailView):
    model = ProductBacklog

    @method_decorator(employee_role_required("product_owner", "scrum_master"))
    def dispatch(self, *args, **kwargs):
        return super(ProductBacklogDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductBacklogDetailView, self).get_context_data(**kwargs)
        # import pdb; pdb.set_trace()
        context['user_stories'] = UserStoryService.product_backlog_stories(
            self.get_object().id
        )
        context['release_list'] = ReleaseBacklogService.product_backlog_releases(
            self.get_object().id
        ).order_by('-id')
        return context