from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from scrum.models import ProductBacklog
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ProductBacklogDeleteView(DeleteView):
    model = ProductBacklog
    success_url = reverse_lazy('hris_productbacklog_list')

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ProductBacklogDeleteView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        product_backlog = self.get_object()
        product_backlog.is_deleted = True
        product_backlog.deleted_by = self.request.user.ProductBacklog
        product_backlog.deleted_on = timezone.now()
        product_backlog.updated_by = self.request.user.ProductBacklog
        product_backlog.save()
        return redirect(self.success_url)