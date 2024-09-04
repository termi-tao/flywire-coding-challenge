from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.admission.models import Course, Intake


class IntakeModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name="INFT101")

    def test_clean(self):
        with self.assertRaises(ValidationError):
            intake = Intake.objects.create(
                course=self.course, start_date="2100-01-01", end_date="2000-01-01"
            )
            intake.save()
