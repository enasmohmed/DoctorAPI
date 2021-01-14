from django.test import SimpleTestCase
from django.urls import reverse, resolve

from Doctor.views import session_list, sessions_details, doctor_list, create_session


class TestUrls(SimpleTestCase):
    # test urls sessions list
    def test_sessions_url_resolves(self):
        url = reverse('doctors:session_home')
        self.assertEquals(resolve(url).func, session_list)


    # test urls sessions details
    def test_sessions_details_url_resolves(self):
        url = reverse('doctors:sessions_details')
        self.assertEquals(resolve(url).func, sessions_details)


    # test urls doctor list
    def test_doctor_url_resolves(self):
        url = reverse('doctors:doctor_list')
        self.assertEquals(resolve(url).func, doctor_list)


    # test urls create sessions
    def test_create_session_url_resolves(self):
        url = reverse('doctors:create_session')
        self.assertEquals(resolve(url).func, create_session)



