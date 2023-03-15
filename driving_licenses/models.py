from django.db import models
from common.models import CommonModel
from datetime import date

class Driving_license(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )

    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="driving_licenses",
    )

    expat_have_driving_license = models.BooleanField(default=False)
    spouse_have_driving_license = models.BooleanField(default=False)

    class FamilyChoices(models.TextChoices):
        EXPAT = ("expat", "Expat")
        SPOUSE = ("spouse", "Spouse")
        
    family = models.CharField(
        max_length=10,
        choices=FamilyChoices.choices,
        blank=True,)

    class VisitChoices(models.TextChoices):
        FIRST_VISIT = ("first_visit", "First visit")
        SECOND_VISIT = ("second_visit", "Second visit")
        
    visit = models.CharField(
        max_length=20,
        choices=VisitChoices.choices,
        blank=True,)

    visit_place = models.CharField(
        max_length=180,
        default="",
    )
    visit_date = models.DateField(("Visit date"), default=date.today)
    visit_time = models.TimeField(("Visit time"), default="19:00")

    explanations = models.ManyToManyField(
        "driving_licenses.Explanation",
        related_name="driving_licenses",
    )
    documents = models.ManyToManyField(
        "driving_licenses.Document",
        related_name="driving_licenses",
    )

    def __str__(self):
        return "Driving_license"
    
    class Meta:
        verbose_name_plural = "Driving_licenses"
    
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