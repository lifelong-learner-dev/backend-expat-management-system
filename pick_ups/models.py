from django.db import models
from common.models import CommonModel
from datetime import date

class Pick_up(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    explanations = models.ManyToManyField(
        "pick_ups.Explanation",
        related_name="pick_ups",
    )

    def total_explanations(process):
        return process.explanations.count()
    
    def __str__(self):
        return "Pick up"
    
    class Meta:
        verbose_name_plural = "Pick ups"

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
    