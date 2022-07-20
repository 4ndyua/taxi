from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin_password",
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username="username",
            password="password",
            license_number="AAAA1234",
        )

    def test_driver_license_number_listed(self):
        url = reverse("admin:taxi_driver_changelist")
        result = self.client.get(url)
        self.assertContains(result, self.driver.license_number)

    def test_driver_additional_info_fieldsets(self):
        url = reverse("admin:taxi_driver_add")
        result = self.client.get(url)
        check_if_exist = (
            "Additional info",
            "first_name",
            "last_name",
            "license_number",
        )
        for part_to_check in check_if_exist:
            self.assertContains(result, part_to_check)
