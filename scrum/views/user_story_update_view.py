from django.views.generic.edit import UpdateView
from scrum.models import UserStory
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class UserStoryUpdateView(UpdateView):
    model = UserStory
    fields = ('title', 'description' )

    @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(UserStoryUpdateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user.employee
        return super(UserStoryUpdateView, self).form_valid(form)
        
    def get_success_url(self):
        success_url = reverse_lazy('scrum_product_backlog', args = [self.get_object().product_backlog.id])
        return success_url