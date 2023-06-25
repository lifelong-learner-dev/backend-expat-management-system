from django.db import models
from common.models import CommonModel
from datetime import date

class Work_permits_process(CommonModel):
    
    title = models.CharField(
        max_length=180,
        default="",
    )
    
    subtitle = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    contents = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    detailed_information = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    subtitle2 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    contents2 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    detailed_information2 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    subtitle3 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    contents3 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    detailed_information3 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    subtitle4 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    contents4 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    detailed_information4 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    subtitle5 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    contents5 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    detailed_information5 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    subtitle6 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    contents6 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    detailed_information6 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    subtitle7 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    contents7 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    detailed_information7 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    subtitle8 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    contents8 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    detailed_information8 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    subtitle9 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    contents9 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    detailed_information9 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    subtitle10 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    contents10 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    detailed_information10 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    responsible_person = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="work_permits_processes",
        default="",
    )

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Work_permits_processes"