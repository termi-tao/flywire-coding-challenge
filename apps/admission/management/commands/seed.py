from django.core.management.base import BaseCommand
from django_seed import Seed
from apps.admission.models import Course, Intake
import string
from random import choice


class Command(BaseCommand):
    help = "Seed the database with random data."

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        # TODO: allow command class to accept CLI parameters
        seeder.add_entity(
            Course,
            5,
            {
                "name": lambda x: seeder.faker.bothify(
                    text="????101", letters=string.ascii_uppercase
                )
            },
        )
        seeder.add_entity(
            Intake,
            10,
            {
                "course": lambda x: choice(list(Course.objects.all())),
                "start_date": lambda x: seeder.faker.date_this_year(),
                "end_date": lambda x: seeder.faker.date_this_year(),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
