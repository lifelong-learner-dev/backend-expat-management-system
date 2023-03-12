from django.db import models
from common.models import CommonModel
from datetime import date


class Moving_company(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    cellphone_number = models.PositiveSmallIntegerField(("Cellphone number"), null=False, default="1",)
    email = models.EmailField(("email address"), blank=True)
    explain = models.CharField(
        max_length=500,
        default="",
    )
    detailed_information = models.CharField(
        max_length=500,
        default="",
    )