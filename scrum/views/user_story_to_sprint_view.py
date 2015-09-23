from scrum.models import UserStory, ProductBacklog, ReleaseBacklog, Sprint
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
import re

class UserStoryToSprintView(View):

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(UserStoryToSprintView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.release_id = kwargs.get('release_id')
        self.release_backlog = ReleaseBacklog.objects.get(id=self.release_id)
        sprint_id = self.request.POST['sprint_id']
        user_stories = self.get_selected_stories(self.request.body)
        try:
            sprint = Sprint.objects.get(id=sprint_id)
            UserStory.objects.filter(id__in=user_stories).update(sprint=sprint)
            messages.add_message(
                self.request, messages.SUCCESS,
                '{0} User Stories successfully moved to sprint {1}'\
                .format(len(user_stories), sprint.name)
            )        
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, str(e))
        return redirect(self.get_success_url())

    def get_selected_stories(self, body):        
        user_stories = [
            int(re.findall(r'\d+', s)[0]) \
            for s in re.findall(r'(user_story=\d+)', body)
        ]
        return user_stories

    def get_success_url(self):
        success_url = reverse_lazy(
            'scrum_product_backlog',
            args = [self.release_backlog.product_backlog.id]
        )
       	return success_url