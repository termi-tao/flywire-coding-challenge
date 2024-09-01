from rest_framework.test import APITestCase
from apps.admission.models import Course
from django.core.management import call_command
from apps.api.views import ListCourses
from rest_framework import status


class ListCoursesTests(APITestCase):
    def setUp(self):
        call_command("loaddata", "../fixtures/api_test_data.json")
        self.courses = Course.objects.all()
        view = ListCourses()
        self.response = view.get({})

    def test_course_count(self):
        course_count = len(self.courses)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(course_count, len(self.response.data))
        self.assertEqual(self.response.data[0]["name"], "INFT101") # per api_test_data.json
