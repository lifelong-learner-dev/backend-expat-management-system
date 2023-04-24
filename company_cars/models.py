from django.db import models
from common.models import CommonModel
from datetime import date

class Company_car(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )

    responsible_person = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="company_cars",
        default="",
    )

    explanations = models.ManyToManyField(
        "company_cars.Explanation",
        related_name="company_cars",
    )
    documents = models.ManyToManyField(
        "company_cars.Document",
        related_name="company_cars",
    )

    def __str__(self):
        return "Company car"
    
    class Meta:
        verbose_name_plural = "Company cars"
    
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