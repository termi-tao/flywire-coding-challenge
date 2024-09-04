from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError


class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Intake(models.Model):
    """Note: Should there be a constrain on the intake overlaps?
    e.g. a course should have only one intake for a period of time.
    Also, should we allow a course having exact the same intakes?
    """

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="intakes")
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=now)

    def clean(self):
        """
        Custom validation to ensure start_date is before end_date.
        """
        super().clean()
        if self.start_date >= self.end_date:
            raise ValidationError(
                {"end_date": "End date must be after the start date."}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
