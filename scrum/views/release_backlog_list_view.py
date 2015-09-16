from django.views.generic import ListView
from scrum.models import ReleaseBacklog
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ReleaseBacklogListView(ListView):
    model = ReleaseBacklog
    queryset = ReleaseBacklog.objects.filter(is_deleted=False)
    paginate_by = 10

    # @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ReleaseBacklogListView, self).dispatch(*args, **kwargs)