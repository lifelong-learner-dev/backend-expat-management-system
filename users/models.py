from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        TR = ("tr", "Turkish")
        EN = ("en", "English")

    class currencyChoices(models.TextChoices):
        USD = ("usd", "USD")
        TL = ("tl", "TL")
        WON = ("won", "WON") 

    class companycarChoices(models.TextChoices):
        GENESIS = ("genesis", "GENESIS")
        SANTAFE = ("santafe", "SANTAFE")
        TUCSON = ("tucson", "TUCSON")
        ELANTRA = ("elantra","ELANTRA")

    avatar = models.ImageField(blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_supporter = models.BooleanField(default=False)
    email = models.EmailField(("email address"), blank=True)
    house_address = models.CharField(max_length=150, blank=True)
    turkish_id = models.SmallIntegerField(("Turkish ID number"), null=False, default="1",)
    tc_id_expiry_date = models.DateField(("TC expiry date"), default=date.today)
    passport_number = models.CharField(max_length=20, blank=True)
    passport_expiry_date = models.DateField(("passport expiry date"), default=date.today)
    car_plate = models.CharField(max_length=20, blank=True)
    company_car_model = models.CharField(
        max_length=10,
        choices=companycarChoices.choices,
        blank=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        blank=True,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        blank=True,
    )
    currency = models.CharField(
        max_length=5,
        choices=currencyChoices.choices,
        blank=True,
    )