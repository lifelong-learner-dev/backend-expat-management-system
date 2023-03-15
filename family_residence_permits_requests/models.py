from django.db import models
from common.models import CommonModel
from datetime import date

class Family_residence_permits_request(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )
    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="family_residence_permits_requests",
    )
    residence_permits = models.ForeignKey(
        "family_residence_permits.Family_residence_permit",
        on_delete=models.CASCADE,
        related_name="family_residence_permits_requests",
    )
    location = models.CharField(
        max_length=180,
        default="",
    )
    date = models.DateField(("When did you lose the card?"), default=date.today)

    class KrstatusChoices(models.TextChoices):
        INFORMED = ("informed", "거주증 카드를 잃어버렸어요")
        CHECKED = ("checked", "총무팀 확인")
        REAPPLIED = ("reapplied", "재신청 완료")
        WAITINGFORAPPROVAL = ("waitingforapproval", "승인 대기 중")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "승인됨 카드 발급 대기 중")
        COMPLETED = ("completed", "카드 발급 및 전달 완료, 모든 절차 완료")

    class EnstatusChoices(models.TextChoices):
        INFORMED = ("informed", "Our family have lost cards")
        CHECKED = ("checked", "GA team member checked the request")
        REAPPLIED = ("reapplied", "Re-applied")
        WAITINGFORAPPROVAL = ("waitingforapproval", "Waiting for approval")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "Approved and waiting for card")
        COMPLETED = ("completed", "Card issued and delivered, Completed")

    class FamilyChoices(models.TextChoices):
        SPOUSE = ("spouse", "Spouse")
        CHILD1 = ("child1", "Child1")
        CHILD2 = ("child2", "Child2")
        CHILD3 = ("child3", "Child3")
        CHILD4 = ("child4", "Child4")

    krstatus = models.CharField(
        max_length=150,
        choices=KrstatusChoices.choices,
        blank=True,)

    enstatus = models.CharField(
        max_length=150,
        choices=EnstatusChoices.choices,
        blank=True,)

    family = models.CharField(
        max_length=10,
        choices=FamilyChoices.choices,
        blank=True,)

    explanations = models.ManyToManyField(
        "family_residence_permits_requests.Explanation",
        related_name="family_residence_permits_requests",
    )
    documents = models.ManyToManyField(
        "family_residence_permits_requests.Document",
        related_name="family_residence_permits_requests",
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Family residence permits requests"
    
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