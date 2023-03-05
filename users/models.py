from django.db import models
from django.contrib.auth.models import AbstractUser

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

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_supporter = models.BooleanField(default=False)
    email = models.EmailField(("email address"), blank=True)
    turkish_id = models.SmallIntegerField(("Turkish ID number"), null=False, default="1",)
    

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=currencyChoices.choices,
    )
