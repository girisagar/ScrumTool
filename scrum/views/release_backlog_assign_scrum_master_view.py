from django.views.generic.edit import UpdateView
from scrum.models import ReleaseBacklog
from hris.models import Role
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from scrum.forms import ScrumMasterForm

class ReleaseBacklogAssignScrumMasterView(UpdateView):
    form_class = ScrumMasterForm
    model = ReleaseBacklog
    template_name = "scrum/releasebacklog_assign_form.html"

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ReleaseBacklogAssignScrumMasterView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user.employee
        employee = form.instance.scrum_master
        scrum_master = Role.objects.get(code="scrum_master")
        employee.roles.add(scrum_master)
        employee.save()
        return super(ReleaseBacklogAssignScrumMasterView, self).form_valid(form)

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, \
            'Scrum Master Successfully Assigned to the {0}'\
            .format(self.get_object().name)
        )
        return reverse_lazy('scrum_product_backlog_detail',\
            args = [self.get_object().product_backlog.id])