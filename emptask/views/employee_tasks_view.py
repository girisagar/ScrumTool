from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from scrum.models import WorkLog
from scrum.services import UserStoryService

class EmployeeTaskTemplateView(TemplateView):
    template_name = "emptask/employeetasks.html"
    
    # @method_decorator(employee_role_required("developer", "tester"))
    def dispatch(self, *args, **kwargs):
        return super(EmployeeTaskTemplateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EmployeeTaskTemplateView, self).get_context_data(**kwargs)
        context['development_tasks'] = UserStoryService.developer_user_stories(
            self.request.user.employee.id
        ).order_by('sprint__id')
        context['testing_tasks'] = UserStoryService.tester_user_stories(
            self.request.user.employee.id
        ).order_by('sprint__id')
        return context