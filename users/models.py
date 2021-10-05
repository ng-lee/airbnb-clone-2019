from django.contrib.auth.models import AbstractUser
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

    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=3, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True
    )
    superhost = models.BooleanField(default=False)
