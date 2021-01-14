from django.test import TestCase, Client, client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Doctor.forms import UserSessionsForm
from Doctor.models import Session, Doctor
from Doctor.serializer import DoctorSerializer
from Doctor.views import DoctorViewSet


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.sessions_url = reverse('doctors:session_home')
        self.sessions_details_url = reverse('doctors:sessions_details')
        self.doctor_list_url = reverse('doctors:doctor_list')
        self.create_session_url = reverse('doctors:create_session')


    # test view session list
    def test_session_list(self):
        response = self.client.get(self.sessions_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    # test view sessions details
    def test_sessions_details(self):
        response = self.client.get(self.sessions_details_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sessions_details.html')


    # test view doctor list
    def test_dector_list(self):
        response = self.client.get(self.doctor_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor_list.html')


    # test view create sessions book
    def test_create_session(self):
        create_session = Session.objects.all()
        form = UserSessionsForm()
        self.assertFalse(form.is_valid())




# test api class doctor view set
class DoctorTestCase(APITestCase):
    def test_doctor(self):
        data = {"name": "testcase", "sessions": "testcase","price": "testcase"}
        response = self.client.post("/api/doctors/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



#test api class Specialty view set
class SpecialtyTestCase(APITestCase):
    def test_specialty(self):
        date = {"name_sp": "testcase", "sep": "testcase"}
        response = self.client.post("/api/specialty/", date)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




#test api class Specialty view set
class SessionTestCase(APITestCase):
    def test_specialty(self):
        date = {"name": "testcase", "title": "testcase"}
        response = self.client.post("/api/sessions/", date)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


