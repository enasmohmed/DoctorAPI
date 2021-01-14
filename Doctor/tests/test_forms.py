from django.test import SimpleTestCase

from Doctor.forms import UserSessionsForm


class TestForms(SimpleTestCase):

    def test_forms(self):
        form_data = {'name': 'name'}
        form = UserSessionsForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

