from django import forms
from hris.models import Employee
from hris.models import Role

class EmployeeForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(
        label="User Roles",
        queryset=Role.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple()
    )

    emp_id = forms.CharField(
        label="EMP ID",
        widget=forms.TextInput({'placeholder': 'EMP-999'}),
        required=True,
    )

    class Meta:
        model = Employee
        exclude = ('user',)
        fields = ('phone', 'street', 'city', 'state', 'zip', 'image', 'emp_id',)

    def save(self):
        return super(EmployeeForm, self).save()