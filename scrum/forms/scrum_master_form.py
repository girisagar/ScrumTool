from django import forms
from hris.models import Employee
from scrum.models import UserStory

class ScrumMasterForm(forms.ModelForm):
    scrum_master = forms.ModelChoiceField(
        label="Scrum Master",
        queryset=Employee.objects.all(),
        required=False
    )

    class Meta:
        model = UserStory
        fields = ('scrum_master',)