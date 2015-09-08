from django import forms
from hris.models import Employee
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class EmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # magic 
        self.user = kwargs['instance'].user
        user_kwargs = kwargs.copy()
        user_kwargs['instance'] = self.user
        self.uf = UserForm(*args, **user_kwargs)
        # magic end 

        super(EmployeeForm, self).__init__(*args, **kwargs)

        self.fields.update(self.uf.fields)
        self.initial.update(self.uf.initial)
         
        # define fields order if needed
        self.fields.keyOrder = (
            'last_name',
            'first_name',
            'second_name',

            "image",
            "street",
            "city",
            "state",
            "zip",

        )

    def save(self, *args, **kwargs):
        # save both forms   
        self.uf.save(*args, **kwargs)
        return super(EmployeeForm, self).save(*args, **kwargs)

    class Meta:
        model = Employee
        fields = ("image", "street", "city", "state", "zip", )