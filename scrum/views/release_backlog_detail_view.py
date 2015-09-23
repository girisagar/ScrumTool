from django.views.generic import DetailView
from scrum.models import ReleaseBacklog
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ReleaseBacklogDetailView(DetailView):
    model = ReleaseBacklog

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ReleaseBacklogDetailView, self).dispatch(*args, **kwargs)