import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from rooms import models as room_models
from users import models as user_models

NAME = "reviews"


class Command(BaseCommand):

    help = f"This command creates many {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help=f"How many {NAME} do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_rooms = room_models.Room.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "user": lambda x: random.choice(all_users),
                "room": lambda x: random.choice(all_rooms),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
