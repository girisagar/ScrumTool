from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from hris.models import Employee
from django.shortcuts import redirect
from django.utils import timezone

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('hris_employee_list')

    def post(self, *args, **kwargs):
        emp_object = self.get_object()
        emp_object.is_deleted = True
        emp_object.deleted_by = self.request.user.employee
        emp_object.deleted_on = timezone.now()
        emp_object.updated_by = self.request.user.employee
        emp_object.save()
        emp_object.user.is_active = False
        emp_object.user.save()
        return redirect(self.success_url)
