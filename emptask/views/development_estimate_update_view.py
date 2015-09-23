from django.views.generic.edit import UpdateView
from scrum.models import WorkLog, UserStory
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.utils import timezone
from django.http import Http404

class DevelopmentEstimateUpdateView(UpdateView):
    model = WorkLog
    template_name = "emptask/development_estimate_daily_form.html"
    fields = ('work_remaining', 'work_done', 'description')

    @method_decorator(employee_role_required("developer"))
    def dispatch(self, *args, **kwargs):
        return super(DevelopmentEstimateUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user.employee
        return super(DevelopmentEstimateUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, \
            'Development Estimation successfully Updated'
        )
        success_url = reverse_lazy(
            'emptask_development_task_detail',
            args=[self.get_object().user_story.id]
        )
        return success_url

    def get_context_data(self, **kwargs):
        context = super(DevelopmentEstimateUpdateView, self).get_context_data(**kwargs)
        context['user_story'] = self.get_object().user_story
        return context