from django.core.management.base import BaseCommand
from rooms import models as room_models

NAME = "room types"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    # def add_arguments(self, parser):
    #     return super().add_arguments(parser)

    def handle(self, *args, **options):
        room_types = [
            "Entire Place",
            "Private Room",
            "Hotel Room",
            "Shared Room",
        ]
        for type in room_types:
            room_models.RoomType.objects.create(name=type)
        self.stdout.write(self.style.SUCCESS(f"{len(room_types)} {NAME} created!"))
