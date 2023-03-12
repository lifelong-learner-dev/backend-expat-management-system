from django.db import models
from common.models import CommonModel
from datetime import date

class Request(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    class RequestsubjectChoices(models.TextChoices):
        GREEN_CARD = ("green_card", "Green card")
        MOVING = ("moving", "Moving")
        PICK_UP = ("pick_up", "Pick up")

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

    request_subject = models.CharField(
        max_length=50,
        choices=RequestsubjectChoices.choices,
        blank=True,)

    green_card_car_insurance_period = models.CharField(
        max_length=50,
        choices=GreencardcarinsuranceperiodChoices.choices,
        blank=True,)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="requests",
        null=True,
        blank=True,
    )
    green_card = models.ForeignKey(
        "green_cards.Green_card",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="requests",
    )
    green_card_departure_date = models.DateField(
        null=True,
        blank=True,
    )
    pick_up = models.ForeignKey(
        "pick_ups.Pick_up",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="requests",
    )
    moving = models.ForeignKey(
        "moving.Moving",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="requests",
    )