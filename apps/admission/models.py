from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, default="unnamed-course")


class Intake(models.Model):
    start_date = models.DateField(default="1800-01-01")
    end_date = models.DateField(default="1800-12-31")
