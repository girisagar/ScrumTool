from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from scrum.models import Sprint
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class SprintDeleteView(DeleteView):
    model = Sprint

    # @method_decorator(employee_role_required("scrum_master"))
    def dispatch(self, *args, **kwargs):
        return super(SprintDeleteView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        sprint = self.get_object()
        sprint.is_deleted = True
        sprint.deleted_by = self.request.user.employee
        sprint.deleted_on = timezone.now()
        sprint.updated_by = self.request.user.employee
        sprint.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        success_url = reverse_lazy('scrum_product_backlog',
            args = [self.get_object().release_backlog.product_backlog.id])
        return success_url