from django.db import models
from common.models import CommonModel
from datetime import date

class Work_permits_request(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )
    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="work_permits_requests",
    )
    location = models.CharField(
        max_length=180,
        default="",
    )
    date = models.DateField(("When did you lose the card?"), default=date.today)

    class KrstatusChoices(models.TextChoices):
        INFORMED = ("informed", "워크퍼밋 카드를 잃어버렸어요")
        CHECKED = ("checked", "총무팀 확인")
        REAPPLIED = ("reapplied", "재신청 완료")
        WAITINGFORAPPROVAL = ("waitingforapproval", "승인 대기 중")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "승인됨 카드 발급 대기 중")
        COMPLETED = ("completed", "카드 발급 및 전달 완료, 모든 절차 완료")

    class EnstatusChoices(models.TextChoices):
        INFORMED = ("informed", "I have lost my card")
        CHECKED = ("checked", "GA team member checked the request")
        REAPPLIED = ("reapplied", "Re-applied")
        WAITINGFORAPPROVAL = ("waitingforapproval", "Waiting for approval")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "Approved and waiting for card")
        COMPLETED = ("completed", "Card issued and delivered, Completed")

    krstatus = models.CharField(
        max_length=150,
        choices=KrstatusChoices.choices,
        blank=True,)

    enstatus = models.CharField(
        max_length=150,
        choices=EnstatusChoices.choices,
        blank=True,)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Work permits requests"
    