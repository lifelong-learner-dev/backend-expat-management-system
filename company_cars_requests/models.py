from django.db import models
from common.models import CommonModel
from datetime import date

class Company_cars_request(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )

    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="company_cars_requests",
    )

    class Accident_locationChoices(models.TextChoices):
        ISTANBUL = ("istanbul", "Istanbul")
        IZMIT = ("izmit", "Izmit")
        
    accident_location = models.CharField(
        max_length=10,
        choices=Accident_locationChoices.choices,
        blank=True,)


    class Accident_typeChoices(models.TextChoices):
        CAR_CRUSH = ("car_crush", "Car crush")
        TOWED_CAR = ("towed_car", "Towed car")
        FLAT_TIRE = ("flat_tire", "Flat tire")
        
    accident_type = models.CharField(
        max_length=10,
        choices=Accident_typeChoices.choices,
        blank=True,)


    class KrstatusChoices(models.TextChoices):
        INFORMED = ("informed", "사고가 났어요")
        CHECKED = ("checked", "총무팀 확인")
        TAKING_NECESSARY_ACTION = ("taking_necessary_action", "필요한 조치 취하는 중")
        COMPLETED = ("completed", "모든 절차 완료")

    class EnstatusChoices(models.TextChoices):
        INFORMED = ("informed", "Informed")
        CHECKED = ("checked", "GA team member checked the request")
        TAKING_NECESSARY_ACTION = ("taking_necessary_action", "Taking necessary action")
        COMPLETED = ("completed", "Completed")
    
    krstatus = models.CharField(
        max_length=100,
        choices=KrstatusChoices.choices,
        default=KrstatusChoices.INFORMED,)

    enstatus = models.CharField(
        max_length=100,
        choices=EnstatusChoices.choices,
        default=EnstatusChoices.INFORMED,)

    explanations = models.ManyToManyField(
        "company_cars_requests.Explanation",
        related_name="company_cars_requests",
    )
    documents = models.ManyToManyField(
        "company_cars_requests.Document",
        related_name="company_cars_requests",
    )

    def __str__(self):
        return "Company cars request"
    
    class Meta:
        verbose_name_plural = "Company cars requests"
    
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