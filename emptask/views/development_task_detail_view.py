from django.views.generic import DetailView
from scrum.models import UserStory
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.core.exceptions import PermissionDenied
from scrum.services import WorkLogService
from django.utils import timezone

class DevelopmentTaskDetailView(DetailView):
    model = UserStory
    template_name = "emptask/development_task_detail.html"

    @method_decorator(employee_role_required("developer"))
    def dispatch(self, *args, **kwargs):
        return super(DevelopmentTaskDetailView, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        instance = self.get_object()
        if not instance.assiged_developer == self.request.user.employee:
            raise PermissionDenied
        return super(DevelopmentTaskDetailView, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        today = timezone.now().date
        development_worklog =  WorkLogService.developer_worklogs(
            self.request.user.employee.id
        ).filter(user_story=self.get_object(), log_type="development")
        context = super(DevelopmentTaskDetailView, self).get_context_data(*args, **kwargs)
        context['today'] = today
        context['development_worklog'] = development_worklog
        context['log_exists_for_today'] =  development_worklog.filter(date=today).exists()
        context['user_story'] = self.get_object()
        return context