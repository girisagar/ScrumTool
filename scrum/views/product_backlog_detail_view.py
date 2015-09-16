from django.views.generic import DetailView
from scrum.models import ProductBacklog
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ProductBacklogDetailView(DetailView):
    model = ProductBacklog

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ProdcuctBacklogDetailView, self).dispatch(*args, **kwargs)