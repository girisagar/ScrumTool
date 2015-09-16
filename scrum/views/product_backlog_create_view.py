from django.views.generic.edit import CreateView
from scrum.models import ProductBacklog
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ProductBacklogCreateView(CreateView):
    model = ProductBacklog
    fields = ('name',)
    success_url = 'scrum_product_backlog_list'

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self,  *args, **kwargs):
        return super(ProductBacklogCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
    	form.instance.owner = self.request.user.employee
    	form.instance.created_by = self.request.user.employee
    	form.instance.updated_by = self.request.user.employee
    	return super(ProductBacklogCreateView, self).form_valid(form)