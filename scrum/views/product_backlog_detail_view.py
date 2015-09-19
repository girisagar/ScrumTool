from django.views.generic import DetailView
from scrum.models import ProductBacklog
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ProductBacklogDetailView(DetailView):
    model = ProductBacklog

    @method_decorator(employee_role_required("product_owner", "scrum_master"))
    def dispatch(self, *args, **kwargs):
        return super(ProductBacklogDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductBacklogDetailView, self).get_context_data(**kwargs)
        # import pdb; pdb.set_trace()
        context['user_stories'] = self.get_object().userstory_set.filter(
            is_deleted=False,
            release_backlog__isnull=True
        )
        context['release_list'] = self.get_object().releasebacklog_set\
            .filter(is_deleted=False).order_by('-id')
        return context
