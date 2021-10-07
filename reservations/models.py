from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models

class Reservation(core_models.TimeStampedModel):
    
    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "comfirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICE = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default=STATUS_PENDING)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
