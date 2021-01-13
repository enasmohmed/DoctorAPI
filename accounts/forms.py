from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models
from django.contrib.auth.models import User


STATES = (
    ('', 'Choose...'),
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient')
)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    case = forms.ChoiceField(choices=STATES)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'case',
            'password'
        ]

    def clean(self, *args, **kwargs):
        case = self.cleaned_data.get('case')
        email_qs = User.objects.filter(email=case)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)



class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

