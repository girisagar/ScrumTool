from django.views.generic import ListView
from scrum.models import ProductBacklog
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ProductBacklogListView(ListView):
    model = ProductBacklog
    queryset = ProductBacklog.objects.filter(is_deleted=False)
    paginate_by = 10

    # @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ProductBacklogListView, self).dispatch(*args, **kwargs)