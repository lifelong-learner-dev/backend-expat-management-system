from django.db import models
from common.models import CommonModel
from datetime import date

class Work_permit(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )
    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="work_permits",
    )
    class KrstatusChoices(models.TextChoices):
        NOT_APPLIIED = ("notapplied", "아직 신청하지 않음")
        APPLIED = ("applied", "신청완료")
        WAITINGFORAPPROVAL = ("waitingforapproval", "승인 대기 중")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "승인됨 카드 발급 대기 중")
        CARDDELIVERED = ("carddelivered", "카드 전달 완료됨")
        COMPLETED = ("completed", "모든 절차 완료")

    class EnstatusChoices(models.TextChoices):
        NOT_APPLIIED = ("notapplied", "Not applied")
        APPLIED = ("applied", "Applied")
        WAITINGFORAPPROVAL = ("waitingforapproval", "Waiting for approval")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "Approved and waiting for card")
        CARDDELIVERED = ("carddelivered", "Card delivered")
        COMPLETED = ("completed", "Completed")

    krstatus = models.CharField(
        max_length=150,
        choices=KrstatusChoices.choices,
        blank=True,)

    enstatus = models.CharField(
        max_length=150,
        choices=EnstatusChoices.choices,
        blank=True,)

    explanations = models.ManyToManyField(
        "work_permits.Explanation",
        related_name="work_permits",
    )

    class Meta:
        verbose_name_plural = "Work permits"
    
    def __str__(self) -> str:
        return self.name

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
    