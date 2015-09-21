from django.views.generic.edit import CreateView
from scrum.models import ReleaseBacklog, ProductBacklog
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ReleaseBacklogCreateView(CreateView):
    model = ReleaseBacklog
    fields = ('name',)

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self,  *args, **kwargs):
        self.product_id = kwargs.get('product_id',None)
        return super(ReleaseBacklogCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user.employee
        form.instance.updated_by = self.request.user.employee
        form.instance.product_backlog_id = self.product_id
        return super(ReleaseBacklogCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # import pdb;pdb.set_trace()
        context = super(ReleaseBacklogCreateView, self).get_context_data(**kwargs)
        try:
            product_obj = ProductBacklog.objects.get(id=self.product_id)
            context['product_obj'] = product_obj
        except Exception, e:
            raise Http404
        return context

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, \
            'New Release Backlog Successfully Added')
        return reverse_lazy('scrum_product_backlog_detail', args = [self.product_id])
