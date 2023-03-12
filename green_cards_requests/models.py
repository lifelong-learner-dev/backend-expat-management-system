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
    class GreencardperiodChoices(models.TextChoices):
        ONE_MONTH = ("one_month", "One month")
        THREE_MONTHS = ("three_months", "Three months")
        SIX_MONTHS = ("six_months", "Six months")
        A_YEAR = ("a_year", "A year")

    class GreencardcarinsuranceperiodChoices(models.TextChoices):
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

    will_you_request_green_card = models.BooleanField(default=False) 
    will_you_request_overseas_car_insurance = models.BooleanField(default=False)
    do_you_have_power_of_attorney = models.BooleanField(default=False)