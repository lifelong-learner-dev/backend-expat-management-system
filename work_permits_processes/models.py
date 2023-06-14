from django.db import models
from common.models import CommonModel
from datetime import date

class Work_permits_process(CommonModel):
    title = models.CharField(
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
        verbose_name_plural = "Work_permits_processes"