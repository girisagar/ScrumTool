from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import DeleteView
from scrum.models import ProductBacklog
from django.shortcuts import redirect
from django.contrib import messages
from django.utils import timezone

class ProductBacklogDeleteView(DeleteView):
    model = ProductBacklog
    success_url = reverse_lazy('scrum_product_backlog_list')

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ProductBacklogDeleteView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        product_backlog_object = self.get_object()
        product_backlog_object.updated_by = self.request.user.employee
        product_backlog_object.is_deleted = True
        product_backlog_object.deleted_by = self.request.user.employee
        product_backlog_object.deleted_on = timezone.now()
        product_backlog_object.save()
        messages.add_message(self.request, messages.SUCCESS, 'New employee successfully added')        
        return redirect(self.success_url)