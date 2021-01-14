from django.urls import path, include
from rest_framework import routers

from . import views
from .views import DoctorViewSet, SpecialtyViewSet, SessionViewSet

app_name = 'Doctor'

router = routers.DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('specialty', SpecialtyViewSet)
router.register('sessions', SessionViewSet)


urlpatterns = [
    path('', views.session_list, name='session_home'),
    path('sessions_details', views.sessions_details, name='sessions_details'),
    path('doctor_list', views.doctor_list, name='doctor_list'),
    path('create_session', views.create_session, name='create_session'),
    path('api/', include(router.urls), name='api_router'),
]


