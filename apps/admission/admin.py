from django.contrib import admin
from .models import Course, Intake
from .utils import generate_admin_operations_links, get_admin_url, get_view_link
from django.utils.html import format_html_join

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # TODO: it'd be handy to have a filter of intakes' start_date/end_date
    list_display = ["name", "display_course_intakes", generate_admin_operations_links]
    search_fields = ["name"]

    @admin.display(description="Intakes (Start Date)")
    def display_course_intakes(self, course):
        """Display course intakes in hyperlinks which are separated by commas.
        Each intake is represented by its own start date.
        TODO: limit the number of intakes or refine content table to avoid redudant info.
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
    list_display = [
        "display_intake_course",
        "start_date",
        "end_date",
        generate_admin_operations_links,
    ]
    list_filter = ["course__name", "start_date", "end_date"]
    # TODO: Find out how to apply autocomplete on search
    search_fields = ["course__name"]

    @admin.display(description="Course")
    def display_intake_course(self, intake):

        return get_view_link(intake.course, intake.course.name, "")

    fields = ["course", "start_date", "end_date"]
