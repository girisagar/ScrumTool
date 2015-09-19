from scrum.models import UserStory, ProductBacklog, ReleaseBacklog
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
import re

class UserStoryToReleaseView(View):

    # @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(UserStoryToReleaseView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.product_id = kwargs.get('product_id')
        product_backlog = ProductBacklog.objects.get(id=self.product_id)
        release_id = self.request.POST['release_backlog']
        user_stories = self.get_selected_stories(self.request.body)
        # import pdb; 
        # pdb.set_trace()
        try:
            release_backlog = ReleaseBacklog.objects.get(id=release_id)
            UserStory.objects.filter(id__in=user_stories).update(release_backlog=release_backlog)
            messages.add_message(
                self.request, messages.SUCCESS,
                '{0} User Stories successfully moved to release {1}'\
                .format(len(user_stories), release_backlog.name)
            )        
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, str(e))
        return redirect(self.get_success_url())

    def get_selected_stories(self, body):        
        user_stories = [
            int(re.findall(r'\d+', s)[0])for s in re.findall(r'(user_story=\d+)', body)
        ]
        return user_stories

    def get_success_url(self):
        success_url = reverse_lazy(
            'scrum_product_backlog',
            args = [self.product_id]
        )
        return success_url
       