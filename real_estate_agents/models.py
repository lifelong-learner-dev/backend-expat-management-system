from django.db import models
from common.models import CommonModel
from datetime import date


class Real_estate_agent(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    responsible_person_name = models.CharField(
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
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Real estate agents"
    