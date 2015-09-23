from django.views.generic import ListView
from scrum.models import ProductBacklog
from scrum.services import ProductBacklogService
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ProductBacklogListView(ListView):
    model = ProductBacklog
    paginate_by = 10

    @method_decorator(employee_role_required("product_owner", "scrum_master"))
    def dispatch(self, *args, **kwargs):
        return super(ProductBacklogListView, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
       	return ProductBacklogService.all()