from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    RATE_ONE = 1
    RATE_TWO = 2
    RATE_THREE = 3
    RATE_FOUR = 4
    RATE_FIVE = 5

    RATE_CHOICES = (
        (RATE_ONE, "1"),
        (RATE_TWO, "2"),
        (RATE_THREE, "3"),
        (RATE_FOUR, "4"),
        (RATE_FIVE, "5"),
    )

    review = models.TextField()
    accuracy = models.IntegerField(choices=RATE_CHOICES)
    communication = models.IntegerField(choices=RATE_CHOICES)
    clearliness = models.IntegerField(choices=RATE_CHOICES)
    location = models.IntegerField(choices=RATE_CHOICES)
    check_in = models.IntegerField(choices=RATE_CHOICES)
    value = models.IntegerField(choices=RATE_CHOICES)

    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.room.name

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.clearliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)
