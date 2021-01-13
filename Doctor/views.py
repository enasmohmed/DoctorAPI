from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from Doctor.forms import UserSessionsForm
from Doctor.models import Session, Doctor, Specialty


# page doctor list
from Doctor.serializer import DoctorSerializer, SpecialtySerializer, SessionSerializer


def doctor_list(request):
    doctor_list = Doctor.objects.all()
    specialty = Specialty.objects.all()
    return render(request, 'doctor_list.html', {'doctor_list': doctor_list, 'specialty':specialty})




# page sessions list
def session_list(request):
    session_list = Session.objects.all()
    doctors = User.objects.all()
    return render(request, 'session_list.html', {'session_list': session_list, 'doctors': doctors})


# page sessions details
def sessions_details(request):
    sessions_details = Session.objects.all()
    return render(request,'sessions_details.html', {'sessions_details': sessions_details})



# create sessions book
def create_session(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserSessionsForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Session Created Successfully')
                return redirect('/')

        else:
            form = UserSessionsForm()
        return render(request, 'create_session.html', {'form': form})
    else:
     return redirect('sessions')




# ViewSets define the view behavior

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class SpecialtyViewSet(ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer



class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer