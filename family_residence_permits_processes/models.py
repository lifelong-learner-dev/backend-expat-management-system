from django.db import models
from common.models import CommonModel
from datetime import date

class Family_residence_permits_process(CommonModel):

    title = models.CharField(
        max_length=180,
        default="",
    )
    subtitle = models.CharField(
        max_length=180,
        default="",
    )

    contents = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information = models.CharField(
        max_length=180,
        default="",
    )

    subtitle2 = models.CharField(
        max_length=180,
        default="",
    )

    contents2 = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information2 = models.CharField(
        max_length=180,
        default="",
    )

    subtitle3 = models.CharField(
        max_length=180,
        default="",
    )

    contents3 = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information3 = models.CharField(
        max_length=180,
        default="",
    )

    subtitle4 = models.CharField(
        max_length=180,
        default="",
    )

    contents4 = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information4 = models.CharField(
        max_length=180,
        default="",
    )

    subtitle5 = models.CharField(
        max_length=180,
        default="",
    )

    contents5 = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information5 = models.CharField(
        max_length=180,
        default="",
    )

    subtitle6 = models.CharField(
        max_length=180,
        default="",
    )

    contents6 = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information6 = models.CharField(
        max_length=180,
        default="",
    )

    subtitle7 = models.CharField(
        max_length=180,
        default="",
    )

    contents7 = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information7 = models.CharField(
        max_length=180,
        default="",
    )

    subtitle8 = models.CharField(
        max_length=180,
        default="",
    )

    contents8 = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information8 = models.CharField(
        max_length=180,
        default="",
    )

    subtitle9 = models.CharField(
        max_length=180,
        default="",
    )

    contents9 = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information9 = models.CharField(
        max_length=180,
        default="",
    )

    subtitle10 = models.CharField(
        max_length=180,
        default="",
    )

    contents10 = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information10 = models.CharField(
        max_length=180,
        default="",
    )

    responsible_person = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="family_residence_permits_processes",
        default="",
    )

    def __str__(self):
        return "Family residence permits process"
    
    class Meta:
        verbose_name_plural = "Family residence permits processes"
