from django.db import models
from common.models import CommonModel
from datetime import date

class Announcement(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )

    class SubjectChoices(models.TextChoices):
        WORK_PERMITS = ("work_permits", "Work permits")
        REAL_ESTATE_AGENTS = ("real_estate_agents", "Real estate agents")
        PICK_UPS = ("pick_ups", "Pick ups")
        MOVING_COMPANIES = ("moving_companies", "Moving companies")
        MOVING = ("moving", "Moving")
        HOUSES = ("houses", "Houses")
        GREEN_CARDS = ("green_cards", "Green cards")
        FAMILY_RESIDENCE_PERMITS = ("family_residence_permtis", "Family residence permits")
        DRIVING_LICENSES = ("driving_licenses", "Driving licenses")
        COMPANY_CARS = ("company_cars", "Company cars")

    subject = models.CharField(
        max_length=30,
        choices=SubjectChoices.choices,
        blank=True,)


    start_date = models.DateField(("Start date?"), default=date.today)
    start_time = models.TimeField(("Start time"), default="19:00")

    finish_date = models.DateField(("Finish date"), default=date.today)
    finish_time = models.TimeField(("Finish time"), default="19:00")

    explanations = models.ManyToManyField(
        "announcements.Explanation",
        related_name="announcements",
    )
    documents = models.ManyToManyField(
        "announcements.Document",
        related_name="announcements",
    )
    visit_place = models.ManyToManyField(
        "announcements.Visit_place",
        related_name="announcements",
    )


    def __str__(self):
        return "Announcement"
    
    class Meta:
        verbose_name_plural = "Announcements"
    
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