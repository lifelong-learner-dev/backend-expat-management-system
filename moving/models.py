from django.db import models
from common.models import CommonModel
from datetime import date

class Moving(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    explanations = models.ManyToManyField(
        "moving.Explanation",
        related_name="moving",
    )

    def total_explanations(moving):
        return moving.explanations.count()
    
    def __str__(self):
        return "Moving"
    
    class Meta:
        verbose_name_plural = "Moving"

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
    