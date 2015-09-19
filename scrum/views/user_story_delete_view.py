from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from scrum.models import UserStory
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class UserStoryDeleteView(DeleteView):
    model = UserStory

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(UserStoryDeleteView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        user_story = self.get_object()
        user_story.is_deleted = True
        user_story.deleted_by = self.request.user.employee
        user_story.deleted_on = timezone.now()
        user_story.updated_by = self.request.user.employee
        user_story.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        success_url = reverse_lazy('scrum_product_backlog', args = [self.get_object().product_backlog.id])
        return success_url