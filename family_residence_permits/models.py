from django.db import models
from common.models import CommonModel
from datetime import date

class Family_residence_permit(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )

    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="family_residence_permits",
    )

    class FamilyChoices(models.TextChoices):
        SPOUSE = ("spouse", "Spouse")
        CHILD1 = ("child1", "Child1")
        CHILD2 = ("child2", "Child2")
        CHILD3 = ("child3", "Child3")
        CHILD4 = ("child4", "Child4")

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class KrstatusChoices(models.TextChoices):
        NOT_APPLIIED = ("notapplied", "아직 신청하지 않음")
        APPLICATIONNEEDED = ("applicationneeded", "신청 필요")
        ANNOUNCEDREQUIREDDOCUMENTS = ("announcedrequireddocuments", "필요서류 및 절차 공지 완료")
        DOCUMENT_DELIVERED = ("documentdeliverd", "서류 전달 완료")
        TRANSLATION = ("translation", "서류 번역 완료")
        NOTARIZATION = ("notarization", "서류 공증 완료")
        APPLIED = ("applied", "신청완료")
        WAITINGFORINTERVIEWDATE = ("waitingforinterviewdate", "이민국 인터뷰 일자 공지 대기중")
        ANNOUNCEDINTERVIEWDATE = ("announcedinterviewdate", "이민국 인터뷰 일자 공지 완료")
        INTERVIEWCOMPLETED = ("interviewcompleted", "이민국 인터뷰 완료")
        REVISITNEEDED = ("revisitneeded", "다시 방문 필요")
        REVISITCOMPLETED = ("revisitcompleted", "재방문 완료")
        WAITINGFORAPPROVAL = ("waitingforapproval", "승인 대기 중")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "승인됨 카드 발급 대기 중")
        CARDDELIVEREDPHOTONEEDED = ("carddeliveredphotoneeded", "카드 전달 완료됨, 총무팀에 거주증 사진 전송 필요")
        POSTOFFICEVISITNEEDED = ("postofficevisitneeded", "부재중으로 인해 우체국 방문 필요")
        COMPLETED = ("completed", "모든 절차 완료")

    class EnstatusChoices(models.TextChoices):
        NOT_APPLIIED = ("notapplied", "Not applied")
        APPLICATIONNEEDED = ("applicationneeded", "Application needed")
        ANNOUNCEDREQUIREDDOCUMENTS = ("announcedrequireddocuments", "Required documents and process were notified")
        DOCUMENT_DELIVERED = ("documentdeliverd", "Document delivered")
        TRANSLATION = ("translation", "Translation completed")
        NOTARIZATION = ("notarization", "Notarization completed")
        APPLIED = ("applied", "Applied")
        WAITINGFORINTERVIEWDATE = ("waitingforinterviewdate", "Waiting for interview date from immigration office")
        ANNOUNCEDINTERVIEWDATE = ("announcedinterviewdate", "immigration office announced interview date")
        INTERVIEWCOMPLETED = ("interviewcompleted", "Interview completed")
        REVISITNEEDED = ("revisitneeded", "Revisit needed")
        REVISITCOMPLETED = ("revisitcompleted", "Revisit completed")
        WAITINGFORAPPROVAL = ("waitingforapproval", "Waiting for approval")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "Approved and waiting for card")
        CARDDELIVEREDPHOTONEEDED = ("carddeliveredphotoneeded", "Card delivered, please send photos to GA team")
        POSTOFFICEVISITNEEDED = ("postofficevisitneeded", "Please visit postoffice")
        COMPLETED = ("completed", "Completed")

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    turkish_id = models.SmallIntegerField(("Turkish ID number"), null=False, default="1",)
    tc_id_expiry_date = models.DateField(("TC expiry date"), default=date.today)
    passport_number = models.CharField(max_length=20, blank=True)
    passport_expiry_date = models.DateField(("Passport expiry date"), default=date.today)
    first_visit_date = models.DateField(("First visit date to Turkiye"), default=date.today)

    family = models.CharField(
        max_length=10,
        choices=FamilyChoices.choices,
        blank=True,)

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        blank=True,)

    krstatus = models.CharField(
        max_length=150,
        choices=KrstatusChoices.choices,
        blank=True,)

    enstatus = models.CharField(
        max_length=150,
        choices=EnstatusChoices.choices,
        blank=True,)
    
    interview_place = models.CharField(
        max_length=180,
        default="",
    )

    interview_date = models.DateField(("Interview date"), default=date.today)
    interview_time = models.TimeField(("Interview time"), default="19:00")

    explanations = models.ManyToManyField(
        "family_residence_permits.Explanation",
        related_name="family_residence_permits",
    )
    documents = models.ManyToManyField(
        "family_residence_permits.Document",
        related_name="family_residence_permits",
    )

    def __str__(self):
        return "Family residence permit"
    
    class Meta:
        verbose_name_plural = "Family residence permits"
    
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