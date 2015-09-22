from django.views.generic import ListView
from scrum.models import ProductBacklog
from scrum.services import ProductBacklogService
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class BurnDownChartListView(ListView):
    model = ProductBacklog
    paginate_by = 10
    template_name = "product_backlog_list.html"

    @method_decorator(employee_role_required("product_owner", "scrum_master", "tester", "developer"))
    def dispatch(self, *args, **kwargs):
        return super(BurnDownChartListView, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
       	return ProductBacklogService.all()