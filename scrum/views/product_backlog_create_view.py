from django.views.generic.edit import CreateView
from scrum.models import ProductBacklog
from django.contrib import messages
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.core.urlresolvers import reverse_lazy

class ProductBacklogCreateView(CreateView):
    model = ProductBacklog
    fields = ('name',)
    success_url = reverse_lazy('scrum_product_backlog_list')

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self,  *args, **kwargs):
        return super(ProductBacklogCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
    	form.instance.owner = self.request.user.employee
    	form.instance.created_by = self.request.user.employee
    	form.instance.updated_by = self.request.user.employee
    	return super(ProductBacklogCreateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'New Prodcuct Backlog successfully added')        
        return reverse_lazy('scrum_product_backlog_list')