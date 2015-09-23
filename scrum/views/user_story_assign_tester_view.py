from django.views.generic.edit import UpdateView
from scrum.models import UserStory
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from scrum.forms import TesterForm

class UserStoryAssignTesterView(UpdateView):
    form_class = TesterForm
    model = UserStory
    # fields = ('scrum_master',)
    template_name = "scrum/userstory_assign_tester_form.html"

    @method_decorator(employee_role_required("scrum_master"))
    def dispatch(self, *args, **kwargs):
        return super(UserStoryAssignTesterView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user.employee
        return super(UserStoryAssignTesterView, self).form_valid(form)


    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, \
            'Tester Successfully Assigned to the User Story{0}'\
            .format(
                self.get_object().title, 
            )
        )
        return reverse_lazy('scrum_product_backlog_detail',\
            args = [self.get_object().product_backlog.id])