from django.views.generic.edit import UpdateView
from scrum.models import ProductBacklog
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ProductBacklogUpdateView(UpdateView):
    model = ProductBacklog
    fields = ('name', )

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ProductBacklogUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'One Prodcuct Backlog successfully updated')        
        return reverse_lazy('scrum_product_backlog_list')