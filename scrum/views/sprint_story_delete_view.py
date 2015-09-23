from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from scrum.models import UserStory
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class SprintStoryDeleteView(DeleteView):
    model = UserStory
    template_name = "scrum/sprint_userstory_confirm_delete.html"
    
    @method_decorator(employee_role_required("scrum_master"))
    def dispatch(self, *args, **kwargs):
        return super(SprintStoryDeleteView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        user_story = self.get_object()
        user_story.updated_by = self.request.user.employee
        user_story.sprint = None
        user_story.assiged_developer = None
        user_story.developer_effort = None
        user_story.assiged_tester = None
        user_story.tester_effort = None
        user_story.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        success_url = reverse_lazy('scrum_product_backlog', args = [self.get_object().product_backlog.id])
        return success_url