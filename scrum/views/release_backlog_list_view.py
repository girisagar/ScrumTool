from django.views.generic import ListView
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from scrum.models import ReleaseBacklog
from scrum.services import ReleaseBacklogService

class ReleaseBacklogListView(ListView):
    model = ReleaseBacklog
    paginate_by = 10

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ReleaseBacklogListView, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        return ReleaseBacklogService.all()