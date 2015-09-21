from django import forms
from hris.models import Employee
from scrum.models import UserStory

class TesterForm(forms.ModelForm):
    assiged_tester = forms.ModelChoiceField(
        label="Assigned Tester",
        queryset=Employee.objects.filter(roles__code__in=['tester']),
        required=False
    )

    class Meta:
        model = UserStory
        fields = ('assiged_tester',)