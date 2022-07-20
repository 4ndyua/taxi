from django.test import TestCase

from taxi.forms import DriverCreationForm


class FormsTests(TestCase):
    def test_driver_creation_form_validation(self):
        form_data = {
            "username": "new_user",
            "password1": "user12345test",
            "password2": "user12345test",
            "first_name": "test_first",
            "last_name": "test_last",
            "license_number": "AAA99999",
        }

        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
