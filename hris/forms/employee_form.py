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

    class Meta:
        model = Employee
        exclude = ('user',  )
        fields = ('street', 'city', 'state', 'zip', 'image' )

    def save(self):
        return super(EmployeeForm, self).save()