from django.db import models
from common.models import CommonModel
from datetime import date

class Additional_information(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )

    subject = models.CharField(
        max_length=180,
        default="",
    ) 

    explanations = models.ManyToManyField(
        "additional_information.Explanation",
        related_name="additional_information",
    )
    documents = models.ManyToManyField(
        "additional_information.Document",
        related_name="additional_information",
    )
    visit_place = models.ManyToManyField(
        "additional_information.Visit_place",
        related_name="additional_information",
    )

    def __str__(self):
        return "Additional information"
    
    class Meta:
        verbose_name_plural = "Additional information"
    
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
    
class Document(CommonModel):
    name = models.CharField(
        max_length=180,
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
        verbose_name_plural = "Documents"

class Visit_place(CommonModel):
    name = models.CharField(
        max_length=180,
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
        verbose_name_plural = "Visit places"