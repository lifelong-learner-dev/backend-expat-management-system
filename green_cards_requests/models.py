from django.db import models
from common.models import CommonModel
from datetime import date

class Green_cards_request(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="green_cards_requests",
    )
    available_country = models.ManyToManyField(
        "green_cards_requests.Available_country",
        related_name="green_cards_requests",
    )
    class GreencardperiodChoices(models.TextChoices):
        FIFTEEN_DAYS = ("fifteen_days", "Fifteen_days")
        ONE_MONTH = ("one_month", "One month")
        THREE_MONTHS = ("three_months", "Three months")
        SIX_MONTHS = ("six_months", "Six months")
        A_YEAR = ("a_year", "A year")

    class GreencardcarinsuranceperiodChoices(models.TextChoices):
        FIFTEEN_DAYS = ("fifteen_days", "Fifteen_days")
        ONE_MONTH = ("one_month", "One month")
        THREE_MONTHS = ("three_months", "Three months")
        SIX_MONTHS = ("six_months", "Six months")
        A_YEAR = ("a_year", "A year")

    green_card_period = models.CharField(
        max_length=50,
        choices=GreencardperiodChoices.choices,
        blank=True,)

    green_card_car_insurance_period = models.CharField(
        max_length=50,
        choices=GreencardcarinsuranceperiodChoices.choices,
        blank=True,)

    green_card_departure_date = models.DateField(
        null=True,
        blank=True,
    )

    green_card_bank_iban_number = models.CharField(
        max_length=180,
        default="",
    )

    green_card_bank_account_name = models.CharField(
        max_length=180,
        default="",
    )

    class CurrencyChoices(models.TextChoices):
        USD = ("usd", "USD")
        TL = ("tl", "TL") 

    currency_green_card = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
        blank=True,
    )

    overseas_car_insurance_bank_iban_number = models.CharField(
        max_length=180,
        default="",
    )

    overseas_car_insurance_bank_account_name = models.CharField(
        max_length=180,
        default="",
    )

    currency_overseas_car_insurance = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
        blank=True,
    )

    power_of_attorney_bank_iban_number = models.CharField(
        max_length=180,
        default="",
    )

    power_of_attorney_bank_account_name = models.CharField(
        max_length=180,
        default="",
    )

    currency_power_of_attorney = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
        blank=True,
    )

    will_you_request_green_card = models.BooleanField(default=False) 
    will_you_request_overseas_car_insurance = models.BooleanField(default=False)
    do_you_have_power_of_attorney = models.BooleanField(default=False)


    def __str__(self):
        return "Green card request"
    
    class Meta:
        verbose_name_plural = "Green card requests"


class Available_country(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    ) 
    description = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "Available country"
    
    class Meta:
        verbose_name_plural = "Available countries"