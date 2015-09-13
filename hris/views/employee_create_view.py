from django.views.generic.edit import CreateView
from hris.models import Employee
from hris.forms import EmployeeForm
from hris.forms import UserForm
from django import forms
from hris.models import Role
from django.http.response import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_form.html'    
    user_form = UserForm

    def post(self, *args, **kwargs):
        return super(EmployeeCreateView, self).post(*args, **kwargs)
        
    def form_valid(self, form):
        import pdb; pdb.set_trace()
        user_form = UserForm(self.request.POST, self.request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            form.instance.user = user
            form.save()
            messages.add_message(self.request, messages.SUCCESS, 'New employee successfully added')
        else:
            messages.add_message(self.request, messages.ERROR, 'Oops!! something went wrong')
            self.set_user_form(user_form)
            return super(EmployeeCreateView, self).form_invalid(form)
        return super(EmployeeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        roles = Role.objects.all()
        context['user_form'] = self.user_form
        context['roles'] = roles
        return context

    def set_user_form(self, form=None):
        self.user_form = form

    def get_success_url(self):
        return reverse('hris_employee_list')