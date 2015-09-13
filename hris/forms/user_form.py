from django import forms
from hris.models import Employee
from django.contrib.auth.models import User
from hris.models import Role
from django.core.exceptions import ValidationError


def validate_email_unique(value):
    exists = User.objects.filter(email=value)
    if exists:
        raise ValidationError("Email address %s already exits, must be unique" % value)

class UserForm(forms.ModelForm): 
    password = forms.CharField(
        required=True, widget=
        forms.PasswordInput(attrs= {'type': 'password'}),
    )
    email = forms.EmailField(
        required=True,
        validators=[validate_email_unique]
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')