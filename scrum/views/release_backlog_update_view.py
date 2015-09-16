from django.views.generic.edit import UpdateView
from scrum.models import ReleaseBacklog
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ReleaseBacklogUpdateView(UpdateView):
    model = ReleaseBacklog
    success_url = reverse_lazy('hris_releasebacklog_list')

    # @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ReleaseBacklogUpdateView, self).dispatch(*args, **kwargs)