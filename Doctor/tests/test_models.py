from django.test import TestCase
from django.urls import reverse

from Doctor.models import Doctor, Specialty, Session


class TestModels(TestCase):


    def test_doctors_models(self):
        entry = Doctor(name="My entry name")
        self.assertEqual(str(entry), entry.name)





