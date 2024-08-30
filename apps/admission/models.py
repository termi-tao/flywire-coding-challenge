from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Intake(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="intakes")
    start_date = models.DateField(default="1800-01-01")
    end_date = models.DateField(default="1800-12-31")
