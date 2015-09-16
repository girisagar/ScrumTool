from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from scrum.models import ReleaseBacklog
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ReleaseBacklogDeleteView(DeleteView):
    model = ProductBacklog
    success_url = reverse_lazy('hris_releasebacklog_list')

    # @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ReleaseBacklogDeleteView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        release_backlog = self.get_object()
        release_backlog.is_deleted = True
        release_backlog.deleted_by = self.request.user.ReleaseBacklog
        release_backlog.deleted_on = timezone.now()
        release_backlog.updated_by = self.request.user.ReleaseBacklog
        release_backlog.save()
        return redirect(self.success_url)