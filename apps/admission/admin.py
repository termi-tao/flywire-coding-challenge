from django.contrib import admin
from .models import Course, Intake
from .utils import display_course_intakes, display_intake_course, view_link
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", display_course_intakes]


@admin.register(Intake)
class IntakeAdmin(admin.ModelAdmin):
    list_display = [display_intake_course, "start_date", "end_date", view_link]
