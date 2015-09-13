from django import forms
from hris.models import Employee
from django.contrib.auth.models import User
from hris.models import Role
from django.core.exceptions import ValidationError


# def validate_email_unique(value):
    # exists = User.objects.filter(email=value)
    # if exists:
    #     raise ValidationError("Email address %s already exits, must be unique" % value)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
    )

    def clean_email(self):
        value = self.cleaned_data['email']
        try:
            exists = User.objects.filter(email = value)
            if not exists:
                return value
            if exists.count()==1 and exists[0].id == self.instance.id:
                return value
        except Exception, e:
            pass
        raise ValidationError("Email address %s already exits, must be unique" % value) 
            
        

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')