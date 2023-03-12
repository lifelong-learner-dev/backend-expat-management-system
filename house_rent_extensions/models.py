from django.db import models
from common.models import CommonModel
from datetime import date


class House_rent_extension(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="house_rent_extensions",
    )

    house = models.ForeignKey(
        "houses.House",
        on_delete=models.CASCADE,
        related_name="house_rent_extensions",
    )

    class KrstatusChoices(models.TextChoices):
        LANDLORD_REQUESTED = ("landlord_requested", "집주인 인상 요청")
        NEGOTIATION = ("negotiation", "집주인과 협상 중")
        COMPLETED = ("completed", "협상 완료") 

    class EnstatusChoices(models.TextChoices):
        LANDLORD_REQUESTED = ("landlord_requested", "Landlord requested rent increase")
        NEGOTIATION = ("negotiation", "Negotiation is ongoing")
        COMPLETED = ("completed", "Negotiation is completed")

    class CurrencyChoices(models.TextChoices):
        USD = ("usd", "USD")
        TL = ("tl", "TL") 

    new_rent_fee = models.SmallIntegerField(("new rent fee"), null=False, default="1",)
    
    currency_new_rent = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
        blank=True,
    )

    limit = models.SmallIntegerField(("Limit"), null=False, default="1",)

    currency_limit = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
        blank=True,
    )

    krstatus = models.CharField(
        max_length = 35,
        choices=KrstatusChoices.choices,
        blank=True,
    )

    enstatus = models.CharField(
        max_length = 35,
        choices=EnstatusChoices.choices,
        blank=True,
    )