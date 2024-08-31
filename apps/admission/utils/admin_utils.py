from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html, format_html_join
from functools import reduce


def get_admin_url(obj, view_name):
    opts = obj._meta
    return reverse(f"admin:{opts.app_label}_{opts.model_name}_{view_name}", args=[obj.pk])


@admin.display(description="Intakes")
def display_course_intakes(course):
    """ Display course intakes in hyperlinks which are separated by commas.
        Each intake is represented by its own start date.
    """
    course_intakes = course.intakes.all()
    return format_html_join(
        ", ",
        "<a href='{}'>{}</a>",
        ((get_admin_url(intake, "change"), intake.start_date) for intake in course_intakes)
    )


@admin.display(description="Course")
def display_intake_course(intake):
    return view_link(intake.course, intake.course.name)


@admin.display(description="Details")
def view_link(obj, text="View"):
    url = get_admin_url(obj, "change")
    return format_html("<a href='{}'>{}</a>", url, text)
