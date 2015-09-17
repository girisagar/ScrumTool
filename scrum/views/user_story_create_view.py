from django.views.generic.edit import CreateView
from scrum.models import UserStory
from django.contrib import messages
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.core.urlresolvers import reverse_lazy

class UserStoryCreateView(CreateView):
    model = UserStory
    fields = ('title', 'description', )

    # @method_decorator(employee_role_required("product_owner"))
    def dispatch(self,  *args, **kwargs):
        return super(UserStoryCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.product_backlog.id = self.kwargs.get('product_id')
        form.instance.created_by = self.request.user.employee
        form.instance.owner = self.request.user.employee
        form.instance.created_by = self.request.user.employee
        form.instance.updated_by = self.request.user.employee
        return super(UserStoryCreateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'New Prodcuct Backlog successfully added')        
        return reverse_lazy('scrum_product_backlog_list')