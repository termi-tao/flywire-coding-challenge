from django.db import models
from django.utils.timezone import now


class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name


class Intake(models.Model):
    """ Note: Should there be a constrain on the intake overlaps?
        e.g. a course should have only one intake for a period of time.
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="intakes")
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=now)
