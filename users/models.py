import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHERS = "others"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHERS, "Others"),
    )

    LANGUAGE_ENG = "eng"
    LANGUAGE_KOR = "kor"

    LANGUAGE_CHOICES = ((LANGUAGE_ENG, "English"), (LANGUAGE_KOR, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=3, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)

    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail(
                "This is for Airbnb Test",
                f"Verify your email, this is your key: {secret}",
                settings.MAIL_FROM,
                [self.email],
            )
        return
