from django.test import TestCase
from apps.admission.models import Course
from django.core.management import call_command
from apps.api.serializers import CourseSerializer
from typing import Dict


class CourseSerializerTests(TestCase):
    def setUp(self):
        call_command("loaddata", "../fixtures/api_test_data.json")
        self.courses = Course.objects.all()

    def tearDown(self):
        Course.objects.all().delete()

    def test_serialization(self):
        data = CourseSerializer(self.courses, many=True).data
        self.assertEqual(len(self.courses), len(data))
        # Test data order
        self.assertEqual(data[0]["name"], "INFT101")
        self.assertEqual(data[1]["name"], "MATH101")

    def test_course_data_attributes(self):
        data = CourseSerializer(self.courses, many=True).data

        def helper(row: Dict) -> None:
            self.assertIn("name", row)
            self.assertIn("intakes", row)
            self.varify_course_intake_data_attributes(row["intakes"])

        map(helper, data)

    def varify_course_intake_data_attributes(self, intakes: Dict):
        def helper(intakes: Dict) -> None:
            # TODO: Should test if it's embedded in the expected course too
            for intake in intakes:
                self.assertIn("start_date", intake)
                self.assertIn("end_date", intake)

        map(helper, intakes)
