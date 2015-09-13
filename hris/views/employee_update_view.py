from django.views.generic.edit import UpdateView
from hris.models import Employee
from hris.forms import EmployeeForm
from hris.forms import UserUpdateForm
from hris.models import Role
from django.http.response import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_form.html'
    user_form = UserUpdateForm

    def form_valid(self, form):
        user_form = self.user_form(self.request.POST, self.request.FILES, instance=self.get_object().user)
        if user_form.is_valid():
            user = user_form.instance.save()
            employee = form.save()
        else:
            messages.add_message(self.request, messages.ERROR, 'Oops!! something went wrong')
            self.set_user_form(user_form)
            return super(EmployeeUpdateView, self).form_invalid(form)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'employee {0} successfully updated'.format(self.get_object().user.get_full_name())
        )
        return super(EmployeeUpdateView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        self.set_user_form()
        context['user_form'] = self.user_form
        return context

    def set_user_form(self, form=None):
        self.user_form = UserUpdateForm(instance=self.get_object().user)

    def get_object(self):
        return self.model.objects.get(pk=self.kwargs.get(self.pk_url_kwarg))

    def get_success_url(self):
        return reverse('hris_employee_list')