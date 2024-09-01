from rest_framework.test import APITestCase
from apps.admission.models import Course
from django.core.management import call_command
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse


class ListCoursesTests(APITestCase):
    def setUp(self):
        call_command("loaddata", "../fixtures/api_test_data.json")
        self.url = reverse("api:list_courses")
        self.courses = Course.objects.all()
        # create a test user for authentication purpose
        self.user = User.objects.create_user(username="testuser", password="testpassword")


    def tearDown(self):
        Course.objects.all().delete()


    def test_authenticated_access(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_unauthenticated_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_list_course(self):
        self.client.force_authenticate(user=self.user)
        course_count = len(self.courses)
        response = self.client.get(self.url)
        self.assertEqual(course_count, len(response.data))
        self.assertEqual(response.data[0]["name"], "INFT101") # per api_test_data.json
