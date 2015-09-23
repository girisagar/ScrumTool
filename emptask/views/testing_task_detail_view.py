from django.views.generic import DetailView
from scrum.models import UserStory
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.core.exceptions import PermissionDenied
from scrum.services import WorkLogService
from django.utils import timezone

class TestingTaskDetailView(DetailView):
    model = UserStory
    template_name = "emptask/testing_task_detail.html"

    @method_decorator(employee_role_required("tester"))
    def dispatch(self, *args, **kwargs):
        print 'here'
        return super(TestingTaskDetailView, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        instance = self.get_object()
        if not instance.assiged_tester == self.request.user.employee:
            raise PermissionDenied
        return super(TestingTaskDetailView, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        today = timezone.now().date
        testing_worklog =  WorkLogService.tester_worklogs(
            self.request.user.employee.id,
        ).filter(user_story=self.get_object(), log_type="test")
        context = super(TestingTaskDetailView, self).get_context_data(*args, **kwargs)
        context['today'] = today
        context['testing_worklog'] = testing_worklog
        context['log_exists_for_today'] =  testing_worklog.filter(date=today).exists()
        context['user_story'] = self.get_object()
        return context