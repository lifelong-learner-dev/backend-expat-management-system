from django.db import models
from common.models import CommonModel
from datetime import date, time

class Moving_preparation_document(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )

    spouse_name = models.CharField(
        max_length=180,
        default="",
    )

    spouse_passport = models.CharField(
        max_length=180,
        default="",
    )

    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="moving_preparation_documents",
    )

    house = models.ForeignKey(
        "houses.House",
        on_delete=models.CASCADE,
        related_name="moving_preparation_documents",
    )

    job_start_date = models.DateField(("Job starting date"), default=date.today)
    job_finish_date = models.DateField(("Job finish date"), default=date.today)

    contents = models.CharField(
        max_length=5000,
        default="",
    )

    signing_authority = models.CharField(
        max_length=180,
        default="",
    )

    certified_translator = models.CharField(
        max_length=180,
        default="",
    )

    class EnsituationsChoices(models.TextChoices):
        EXPATRIATION = ("expatriation", "Expatriation")
        REPATRIATION = ("repatriation", "Repatriation")

    ensituation = models.CharField(
        max_length=150,
        choices=EnsituationsChoices.choices,
        blank=True,)