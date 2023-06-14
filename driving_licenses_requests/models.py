from django.db import models
from common.models import CommonModel
from datetime import date

class Driving_licenses_request(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )

    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="driving_licenses_requests",
    )

    class FamilyChoices(models.TextChoices):
        EXPAT = ("expat", "Expat")
        SPOUSE = ("spouse", "Spouse")
        
    family = models.CharField(
        max_length=10,
        choices=FamilyChoices.choices,
        blank=True,)

    lost_location = models.CharField(
        max_length=180,
        default="",
    )
    lost_date = models.DateField(("When did you lose the card?"), default=date.today)

    revisit_date = models.DateField(("Register office revisit date"), default=date.today)
    revisit_time = models.TimeField(("Register office revisit time"), default="19:00")
    revisit_place = models.CharField(
        max_length=180,
        default="",
    )

    class KrstatusChoices(models.TextChoices):
        INFORMED = ("informed", "튀르키예 운전면허증을 잃어버렸어요")
        CHECKED = ("checked", "총무팀 확인")
        ANNOUNCEMENT_VISIT_SCHEDULE = ("announcement_visit_schedule", "인구시민청 방문 관련 공지")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "승인됨 카드 발급 대기 중")
        COMPLETED = ("completed", "카드 발급 및 전달 완료, 모든 절차 완료")

    class EnstatusChoices(models.TextChoices):
        INFORMED = ("informed", "I have lost card")
        CHECKED = ("checked", "GA team member checked the request")
        ANNOUNCEMENT_VISIT_SCHEDULE = ("announcement_visit_schedule", "Visiting schedule of register office notified")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "Approved and waiting for car to be delivered")
        COMPLETED = ("completed", "Completed")
    
    krstatus = models.CharField(
        max_length=100,
        choices=KrstatusChoices.choices,
        default=KrstatusChoices.INFORMED,)

    enstatus = models.CharField(
        max_length=100,
        choices=EnstatusChoices.choices,
        default=EnstatusChoices.INFORMED,)


    def __str__(self):
        return "Driving licenses request"
    
    class Meta:
        verbose_name_plural = "Driving licenses requests"
    
