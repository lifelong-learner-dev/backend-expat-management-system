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
        NOT_APPLIED = ("notapplied", "아직 신청하지 않음")
        WAITINGFORAPPROVAL = ("waitingforapproval", "신청 완료, 승인 대기 중")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "승인됨 카드 발급 대기 중")
        CARDDELIVERED = ("carddelivered", "카드 전달 완료됨")
        COMPLETED = ("completed", "모든 절차 완료, 현재 연장 필요 없음")

    class EnstatusChoices(models.TextChoices):
        NOT_APPLIED = ("notapplied", "Not applied")
        WAITINGFORAPPROVAL = ("waitingforapproval", "Applied and Waiting for approval")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "Approved and waiting for card")
        CARDDELIVERED = ("carddelivered", "Card delivered")
        COMPLETED = ("completed", "Completed, No need to apply for extension yet")
        

    krstatus = models.CharField(
        max_length=150,
        choices=KrstatusChoices.choices,
        blank=True,)


    enstatus = models.CharField(
        max_length=150,
        choices=EnstatusChoices.choices,
        blank=True,)

    def save(self, *args, **kwargs):
        mapping = {
                self.EnstatusChoices.NOT_APPLIED: self.KrstatusChoices.NOT_APPLIED,
                self.EnstatusChoices.WAITINGFORAPPROVAL: self.KrstatusChoices.WAITINGFORAPPROVAL,
                self.EnstatusChoices.APPROVEDANDWAITFORCARD: self.KrstatusChoices.APPROVEDANDWAITFORCARD,
                self.EnstatusChoices.CARDDELIVERED: self.KrstatusChoices.CARDDELIVERED,
                self.EnstatusChoices.COMPLETED: self.KrstatusChoices.COMPLETED,
        }
        self.krstatus = mapping.get(self.enstatus, '')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Work permits"
    
    def __str__(self) -> str:
        return self.name
    