from django.contrib import admin
from .models import Course, Intake
from .utils import entry_operations, get_admin_url, get_view_link
from django.utils.html import format_html_join

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "display_course_intakes", entry_operations]

    @admin.display(description="Intakes")
    def display_course_intakes(self, course):
        """Display course intakes in hyperlinks which are separated by commas.
        Each intake is represented by its own start date.
        """
        course_intakes = course.intakes.all()
        return format_html_join(
            ", ",
            "<a href='{}'>{}</a>",
            (
                (get_admin_url(intake, "change"), intake.start_date)
                for intake in course_intakes
            ),
        )


@admin.register(Intake)
class IntakeAdmin(admin.ModelAdmin):
    list_display = ["display_intake_course", "start_date", "end_date", entry_operations]

    @admin.display(description="Course")
    def display_intake_course(self, intake):

        return get_view_link(intake.course, intake.course.name, "")
