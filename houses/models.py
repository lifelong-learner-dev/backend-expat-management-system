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

    clauses = models.ManyToManyField(
        "houses.Clause",
        related_name="houses",
    )

    explanations = models.ManyToManyField(
        "houses.Explanation",
        related_name="houses",
    )

    def total_explanations(house):
        return house.explanations.count()

    regulations = models.ManyToManyField(
        "houses.Regulation",
        related_name="houses",
    )

    def total_regulations(house):
        return house.regulations.count()
    
    def __str__(self):
        return "House"
    
    class Meta:
        verbose_name_plural = "Houses"

class Clause(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    ) 
    krclause = models.CharField(
        max_length=500,
        null=True,
        blank=True,
    )
    trclause = models.CharField(
        max_length=500,
        null=True,
        blank=True,
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Clauses"

class Explanation(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    ) 
    description = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    detailed_information = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Explanations"
    
class Regulation(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    ) 
    description = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    detailed_information = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Regulations"