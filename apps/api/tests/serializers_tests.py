from django.test import TestCase
from apps.admission.models import Course
from django.core.management import call_command
from apps.api.serializers import CourseSerializer
from typing import Dict


class CourseSerializerTests(TestCase):
    def setUp(self):
        call_command("loaddata", "../fixtures/api_test_data.json")
        self.courses = Course.objects.all()
        self.data = CourseSerializer(self.courses, many=True).data

    def tearDown(self):
        Course.objects.all().delete()

    def test_serialization(self):
        self.data = CourseSerializer(self.courses, many=True).data
        self.assertEqual(len(self.courses), len(self.data))
        # Test data order
        self.assertEqual(self.data[0]["name"], "INFT101")
        self.assertEqual(self.data[1]["name"], "MATH101")
        self.assertEqual(self.data[-1]["name"], "ABCD101")
        self.assertEqual(self.data[-2]["name"], "SYST101")

    def test_course_data_attributes(self):
        self.data = CourseSerializer(self.courses, many=True).data
        def helper(row: Dict) -> None:
            self.assertIn("name", row)
            self.assertIn("intakes", row)
            self.varify_course_intake_data_attributes(row["intakes"])

        map(helper, self.data)

    def varify_course_intake_data_attributes(self, intakes: Dict):
        # TODO: Should create tests for the helper function when logic expands
        def helper(intakes: Dict) -> None:
            # TODO: Should test if intake is embedded in the expected course too
            for intake in intakes:
                self.assertIn("start_date", intake)
                self.assertIn("end_date", intake)

        map(helper, intakes)
