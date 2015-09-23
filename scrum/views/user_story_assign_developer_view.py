from django.views.generic.edit import UpdateView
from scrum.models import UserStory
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from scrum.forms import DeveloperForm

class UserStoryAssignDeveloperView(UpdateView):
    form_class = DeveloperForm
    model = UserStory
    # fields = ('scrum_master',)
    template_name = "scrum/userstory_assign_developer_form.html"

    @method_decorator(employee_role_required("scrum_master"))
    def dispatch(self, *args, **kwargs):
        return super(UserStoryAssignDeveloperView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user.employee
        return super(UserStoryAssignDeveloperView, self).form_valid(form)


    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, \
            'Developer Successfully Assigned to the User Story{0}'\
            .format(self.get_object().title)
        )
        return reverse_lazy('scrum_product_backlog_detail',\
            args = [self.get_object().product_backlog.id])