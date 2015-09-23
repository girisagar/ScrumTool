from django.views.generic.edit import CreateView
from scrum.models import WorkLog, UserStory
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.utils import timezone
from django.http import Http404

class TestingEstimateCreateView(CreateView):
    model = WorkLog
    template_name = "emptask/testing_estimate_daily_form.html"
    fields = ('work_remaining', 'work_done', 'description')

    @method_decorator(employee_role_required("tester"))
    def dispatch(self, *args, **kwargs):
        return super(TestingEstimateCreateView, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        story_id = kwargs['story_id']        
        try:
            self.user_story = UserStory.objects.get(pk=story_id)
        except:
            raise Http404
        return super(TestingEstimateCreateView, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        story_id = kwargs['story_id']        
        try:
            self.user_story = UserStory.objects.get(pk=story_id)
        except:
            raise Http404
        return super(TestingEstimateCreateView, self).post(*args, **kwargs)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user.employee
        form.instance.created_by = self.request.user.employee
        form.instance.employee = self.request.user.employee
        form.instance.user_story = self.user_story
        form.instance.log_type = 'test'
        return super(TestingEstimateCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(TestingEstimateCreateView, self).get_context_data(**kwargs)
        context['user_story'] = self.user_story
        return context
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, \
            'Testing Estimation successfully Updated'
        )
        success_url = reverse_lazy('emptask_testing_task_detail', args=[self.user_story.id])
        return success_url