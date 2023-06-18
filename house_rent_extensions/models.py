from django.db import models
from common.models import CommonModel
from datetime import date


class House_rent_extension(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    responsible_person = models.ForeignKey(
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

    def save(self, *args, **kwargs):
        mapping = {
                self.EnstatusChoices.LANDLORD_REQUESTED: self.KrstatusChoices.LANDLORD_REQUESTED,
                self.EnstatusChoices.NEGOTIATION: self.KrstatusChoices.NEGOTIATION,
                self.EnstatusChoices.COMPLETED: self.KrstatusChoices.COMPLETED,
        }
        self.krstatus = mapping.get(self.enstatus, '')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
        
    class Meta:
        verbose_name_plural = "House rent extensions"