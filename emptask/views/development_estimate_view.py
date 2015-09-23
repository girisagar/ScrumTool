from django.views.generic.edit import UpdateView
from scrum.models import UserStory, WorkLog
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.utils import timezone

class DevelopmentEstimateView(UpdateView):
    model = UserStory
    template_name = "emptask/testing_estimate_form.html"
    fields = ('developer_effort', )

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(DevelopmentEstimateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user.employee
        worklog, created = WorkLog.objects.get_or_create(
            employee=self.request.user.employee,
            user_story=self.get_object(),
            date=timezone.now(),            
            log_type = 'development'
        )
        # import pdb;
        # pdb.set_trace()
        if created:
            worklog.created_by = self.request.user.employee
        worklog.work_remaining = form.cleaned_data['developer_effort']
        worklog.work_done = 0
        worklog.description = "User Story Task started"
        worklog.save()
        return super(DevelopmentEstimateView, self).form_valid(form)
        
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, \
            'Test Estimation successfully Updated'
        )
        success_url = reverse_lazy('emptask_mytask')
        return success_url