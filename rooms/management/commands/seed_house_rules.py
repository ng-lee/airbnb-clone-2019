from django.core.management.base import BaseCommand
from rooms import models as room_models

NAME = "house rules"


class Command(BaseCommand):

    help = "This command creates amenities"

    # def add_arguments(self, parser):
    #     return super().add_arguments(parser)

    def handle(self, *args, **options):
        house_rules = [
            "No parties or events allowed",
            "No smoking allowed",
            "No pets allowed",
            "Suitable for toddlers and children under 12",
            "No unregistered guests allowed",
            "Please don’t eat or drink in the bedrooms",
            "Please respect the noise curfew",
            "Please turn off the AC when you go out",
            "Please respect check-in and check-out times",
            "Please take extra care of your keys",
            "Please take care of the furnishings",
            "Please don’t rearrange the furniture",
            "Please do your dishes",
            "Please take the trash out before you leave",
            "No illegal substances allowed on the premises",
        ]
        for rule in house_rules:
            room_models.HouseRule.objects.create(name=rule)
        self.stdout.write(self.style.SUCCESS(f"{len(house_rules)} {NAME} created!"))
