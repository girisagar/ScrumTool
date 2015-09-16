from django.views.generic.edit import CreateView
from scrum.models import ProductBacklog
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ProductBacklogCreateView(CreateView):
    model = ProductBacklog
    fields = ('name',)

    # @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ProductBacklogCreateView, self).dispatch(*args, **kwargs)