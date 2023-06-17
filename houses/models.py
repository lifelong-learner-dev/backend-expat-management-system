from django.db import models
from common.models import CommonModel
from datetime import date


class House(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="houses",
        default=""
    )
    current_rent_fee = models.SmallIntegerField(("Current rent fee"), null=False, default="1",)

    class CurrencyChoices(models.TextChoices):
        USD = ("usd", "USD")
        TL = ("tl", "TL") 

    currency_rent = models.CharField(
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
    
    def __str__(self):
        return "House"
    
    class Meta:
        verbose_name_plural = "Houses"