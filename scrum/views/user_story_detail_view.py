from django.views.generic import DetailView
from scrum.models import UserStory
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class UserStoryDetailView(DetailView):
    model = UserStory

    @method_decorator(employee_role_required("product_owner", "scrum_master"))
    def dispatch(self, *args, **kwargs):
    	print 'here'
        return super(UserStoryDetailView, self).dispatch(*args, **kwargs)
