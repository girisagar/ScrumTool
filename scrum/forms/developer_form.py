from django import forms
from hris.models import Employee
from scrum.models import Sprint

class DeveloperForm(forms.ModelForm):
    assiged_developer = forms.ModelChoiceField(
        label="Assigned Developer",
        queryset=Employee.objects.filter(roles__code__in=['developer']),
        required=False
    )

    class Meta:
        model = Sprint
        fields = ('assiged_developer',)