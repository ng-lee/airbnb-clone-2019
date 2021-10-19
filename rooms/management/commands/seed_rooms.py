import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models

NAME = "rooms"


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
        all_room_types = room_models.RoomType.objects.all()
        all_amenities = room_models.Amenity.objects.all()
        all_facilities = room_models.Facility.objects.all()
        all_house_rules = room_models.HouseRule.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(all_room_types),
                "guests": lambda x: random.randint(2, 11),
                "price": lambda x: random.randint(0, 300),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": random.randint(0, 5),
                "baths": random.randint(0, 5),
            },
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            room = room_models.Room.objects.get(pk=pk)
            for _ in range(2, random.randint(5, 16)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photo/{random.randint(1, 31)}.webp",
                )

            for a in all_amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2:
                    room.amenities.add(a)
            for f in all_facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2:
                    room.facilities.add(f)
            for r in all_house_rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
