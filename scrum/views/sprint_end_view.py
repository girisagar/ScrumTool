from django.views.generic.edit import UpdateView
from scrum.models import Sprint
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.utils import timezone
from django.shortcuts import redirect

class SprintEndView(UpdateView):
    model = Sprint
    template_name = "scrum_sprint_end.html"

    @method_decorator(employee_role_required("scrum_master"))
    def dispatch(self, *args, **kwargs):
        return super(SprintEndView, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        instance = self.get_object()
        if instance.sprint_end:
            message = 'Sprint Already Ended'
            return redirect(self.get_success_url(message))
        instance.updated_by = self.request.user.employee
        instance.sprint_end = timezone.now()
        instance.save()
        return redirect(self.get_success_url())

    def get_success_url(self, message='Sprint successfully Ended'):
        messages.add_message(self.request, messages.SUCCESS, \
            message
        )       
        success_url = reverse_lazy('scrum_product_backlog',
            args = [self.get_object().release_backlog.product_backlog.id]
        )
        return success_url