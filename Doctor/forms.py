from django.forms import ModelForm

from Doctor.models import Session


class UserSessionsForm(ModelForm):
    class Meta:
        model = Session
        fields = '__all__'
