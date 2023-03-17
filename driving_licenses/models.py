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


    biometric_photo = models.BooleanField(default=False)
    house_address_registration_driving_license = models.BooleanField(default=False)
    notarized_driving_license = models.BooleanField(default=False)
    graduation_certificate_driving_license = models.BooleanField(default=False)
    health_report_driving_license = models.BooleanField(default=False)
    driving_license_exchange_fee = models.BooleanField(default=False)

    class KrstatusChoices(models.TextChoices):
        PLEASE_SEND_SCANNED_KOREAN_DRIVING_LICENSE = ("please_send_scanned_korean_driving_license", "스캔하신 운전면허증 앞, 뒷면을 총무팀에 보내주세요")
        ONGOING_KOREAN_DRIVING_LICENSE_TRANSLATION = ("ongoing_korean_driving_license_translation", "운전면허증 번역 중")
        COMPLETED_NOTARIZATION_KOREAN_DRIVING_LICENSE_TRANSLATION = ("completed_notarization_korean_driving_license_translation", "운전면허증 번역 공증 완료")
        PLEASE_SEND_SCANNED_GRADUATION_CERTIFICATE = ("please_send_scanned_graduation_certificate", "스캔하신 졸업증명서를 총무팀에 보내주세요")
        ONGOING_GRADUATION_CERTIFICATE_TRANSLATION = ("ongoing_graduation_certificate_translation", "졸업증명서 번역 중")
        COMPLETED_NOTARIZATION_GRADUATION_CERTIFICATE_TRANSLATION = ("completed_notarization_graduation_certificate_translation", "졸업증명서 번역 공증 완료")
        PLEASE_VISIT_POST_OFFICE = ("please_visit_post_office", "e-devlet 비밀번호 발급을 위해 우체국을 방문하세요")
        ONGOING_HOUSE_ADDRESS_REGISTRATION = ("ongoing_house_address_registration", "거주증 등록 진행 중")
        COMPLETED_HOUSE_ADDRESS_REGISTRATION = ("completed_house_address_registration", "거주증 등록 완료")
        ANNOUNCEMENT_FIRST_VISIT_SCHEDULE = ("announcement_first_visit_schedule", "인구시민청 첫방문 관련 공지")
        FIRST_VISIT = ("first_visit", "첫번째 방문")
        PLEASE_VISIT_HOSPITAL_FOR_HEALTH_REPORT = ("please_visit_hospital_for_health_report", "건강진단서를 위해 병원을 방문하세요")
        PLEASE_PAY_DRIVING_LICENSE_EXCHANGE_COST = ("please_pay_driving_license_exchange_cost", "운전면허증 교환 수수료를 납부하세요")
        ANNOUNCEMENT_SECOND_VISIT_SCHEDULE = ("announcement_second_visit_schedule", "인구시민청 두번째방문 관련 공지")
        SECOND_VISIT = ("second_visit", "두번째 방문")
        REVISIT_NEEDED = ("revisit_needed", "재방문 필요")
        TEMPORARY_CARD = ("temporary_card", "임시 운전면허증 발급")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "승인됨 카드 발급 대기 중")
        COMPLETED = ("completed", "카드 발급 및 전달 완료, 모든 절차 완료")

    krstatus = models.CharField(
        max_length=500,
        choices=KrstatusChoices.choices,
        blank=True,)

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
    when_was_your_first_entry_date = models.DateField(("When was your first entry date?"), default=date.today)

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
    visit_place = models.ManyToManyField(
        "driving_licenses.Visit_place",
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