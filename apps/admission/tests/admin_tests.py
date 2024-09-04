from django.test import TestCase
from apps.admission.models import Intake, Course
from django.contrib import admin
from apps.admission.admin import CourseAdmin, IntakeAdmin
from django.apps import apps


class AdminTests(TestCase):

    def setUp(self):
        self.course = Course.objects.create(name="INFT101")
        self.intake_1 = Intake.objects.create(
            course=self.course, start_date="2020-01-01", end_date="2020-03-01"
        )
        self.intake_2 = Intake.objects.create(
            course=self.course, start_date="2020-05-01", end_date="2020-08-01"
        )
        self.app_name = apps.get_app_config("admission").name.split(".")[-1]
        self.admin_site = admin.site
        # TODO: Find an easier way to mock admin site
        self.course_admin = CourseAdmin(Course, self.admin_site)
        self.intake_admin = IntakeAdmin(Intake, self.admin_site)

    def tearDown(self):
        Course.objects.all().delete()
        Intake.objects.all().delete()

    def test_display_course_intakes(self):
        intake_1_url = f"/admin/{self.app_name}/{Intake._meta.model_name}/1/change/"
        intake_2_url = f"/admin/{self.app_name}/{Intake._meta.model_name}/2/change/"
        self.assertEqual(
            self.course_admin.display_course_intakes(self.course),
            f"<a href='{intake_1_url}'>{self.intake_1.start_date}</a>, <a href='{intake_2_url}'>{self.intake_2.start_date}</a>",
        )

    def test_display_intake_course(self):
        url = f"/admin/{self.app_name}/{Course._meta.model_name}/1/change/"
        self.assertEqual(
            f"<a class='' href='{url}'>{self.intake_1.course.name}</a>",
            self.intake_admin.display_intake_course(self.intake_1),
        )
