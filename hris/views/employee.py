from django.views.generic.edit import CreateView
from django.views.generic import ListView
from hris.models import Employee
from hris.forms import EmployeeForm
from hris.forms import UserForm
from django import forms
from hris.models import Role
from django.http.response import HttpResponse
from django.core.urlresolvers import reverse

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_wizard.html'
    user_form = UserForm

    def form_valid(self, form):
        user_form = UserForm(self.request.POST, self.request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            form.instance.user = user
            employee = form.save()
            return HttpResponse('SuccessFull !!!')
        self.set_user_form(user_form)
        return super(EmployeeCreateView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        roles = Role.objects.all()
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        context['user_form'] = self.user_form
        context['roles'] = roles
        return context

    def set_user_form(self, form=None):
        self.user_form = form

    def get_success_url(self):
        return reverse('hris_home')

class EmployeeListView(ListView):
    template_name = 'employee/employee_list.html'
    model = Employee