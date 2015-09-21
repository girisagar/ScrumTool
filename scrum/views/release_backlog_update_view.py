from django.views.generic.edit import UpdateView
from scrum.models import ReleaseBacklog
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ReleaseBacklogUpdateView(UpdateView):
    model = ReleaseBacklog
    fields = ('name', )
    success_url = reverse_lazy('hris_releasebacklog_list')

    # @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ReleaseBacklogUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user.employee
        return super(ReleaseBacklogUpdateView, self).form_valid(form)


    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, \
            'Release Backlog Successfully Updated')
        return reverse_lazy('scrum_product_backlog_detail',\
            args = [self.get_object().product_backlog.id])