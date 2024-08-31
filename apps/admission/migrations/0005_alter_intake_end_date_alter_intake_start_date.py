# Generated by Django 5.0.8 on 2024-08-31 08:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0004_intake_course_alter_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intake',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='intake',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
