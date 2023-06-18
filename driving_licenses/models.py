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
        PLEASE_PAY_DRIVING_LICENSE_EXCHANGE_COST = ("please_pay_driving_license_exchange_cost", "운전면허증 교환 수수료를 납부하세요")
        ANNOUNCEMENT_SECOND_VISIT_SCHEDULE = ("announcement_second_visit_schedule", "인구시민청 두번째방문 관련 공지")
        SECOND_VISIT = ("second_visit", "두번째 방문")
        REVISIT_NEEDED = ("revisit_needed", "재방문 필요")
        TEMPORARY_CARD = ("temporary_card", "임시 운전면허증 발급")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "승인됨 카드 발급 대기 중")
        COMPLETED = ("completed", "카드 발급 및 전달 완료, 모든 절차 완료")

    class EnstatusChoices(models.TextChoices):
        PLEASE_SEND_SCANNED_KOREAN_DRIVING_LICENSE = ("please_send_scanned_korean_driving_license", "Please send scanned Korean driving license")
        ONGOING_KOREAN_DRIVING_LICENSE_TRANSLATION = ("ongoing_korean_driving_license_translation", "Korean driving license translation in progress")
        COMPLETED_NOTARIZATION_KOREAN_DRIVING_LICENSE_TRANSLATION = ("completed_notarization_korean_driving_license_translation", "Korean driving license translation has been completed and notarized")
        PLEASE_SEND_SCANNED_GRADUATION_CERTIFICATE = ("please_send_scanned_graduation_certificate", "Please send scanned graduation certificate")
        ONGOING_GRADUATION_CERTIFICATE_TRANSLATION = ("ongoing_graduation_certificate_translation", "Graduation certificate translation in progress")
        COMPLETED_NOTARIZATION_GRADUATION_CERTIFICATE_TRANSLATION = ("completed_notarization_graduation_certificate_translation", "Graduation certificate translation has been completed and notarized")
        PLEASE_VISIT_POST_OFFICE = ("please_visit_post_office", "Please visit post office for issuing e-devlet password")
        ONGOING_HOUSE_ADDRESS_REGISTRATION = ("ongoing_house_address_registration", "House address registration in progress")
        COMPLETED_HOUSE_ADDRESS_REGISTRATION = ("completed_house_address_registration", "House address registration has been completed")
        ANNOUNCEMENT_FIRST_VISIT_SCHEDULE = ("announcement_first_visit_schedule", "Announcement of the schedule for the first visit to the registration office")
        FIRST_VISIT = ("first_visit", "First visit")
        PLEASE_PAY_DRIVING_LICENSE_EXCHANGE_COST = ("please_pay_driving_license_exchange_cost", "Please pay driving license exchange cost")
        ANNOUNCEMENT_SECOND_VISIT_SCHEDULE = ("announcement_second_visit_schedule", "Announcement of the schedule for the second visit to the registration office")
        SECOND_VISIT = ("second_visit", "Second visit")
        REVISIT_NEEDED = ("revisit_needed", "Revisit needed")
        TEMPORARY_CARD = ("temporary_card", "Temporary card has been issued")
        APPROVEDANDWAITFORCARD = ("approvedandwaitforcard", "Approved and waiting for issuing card")
        COMPLETED = ("completed", "Card issued and sent it to you. All processes are completed.")

    krstatus = models.CharField(
        max_length=500,
        choices=KrstatusChoices.choices,
        default=KrstatusChoices.PLEASE_SEND_SCANNED_KOREAN_DRIVING_LICENSE,)

    enstatus = models.CharField(
        max_length=500,
        choices=EnstatusChoices.choices,
        default=EnstatusChoices.PLEASE_SEND_SCANNED_KOREAN_DRIVING_LICENSE,)

    def save(self, *args, **kwargs):
        mapping = {
                self.EnstatusChoices.PLEASE_SEND_SCANNED_KOREAN_DRIVING_LICENSE: self.KrstatusChoices.PLEASE_SEND_SCANNED_KOREAN_DRIVING_LICENSE,
                self.EnstatusChoices.ONGOING_KOREAN_DRIVING_LICENSE_TRANSLATION: self.KrstatusChoices.ONGOING_KOREAN_DRIVING_LICENSE_TRANSLATION,
                self.EnstatusChoices.COMPLETED_NOTARIZATION_KOREAN_DRIVING_LICENSE_TRANSLATION: self.KrstatusChoices.COMPLETED_NOTARIZATION_KOREAN_DRIVING_LICENSE_TRANSLATION,
                self.EnstatusChoices.PLEASE_SEND_SCANNED_GRADUATION_CERTIFICATE: self.KrstatusChoices.PLEASE_SEND_SCANNED_GRADUATION_CERTIFICATE,
                self.EnstatusChoices.ONGOING_GRADUATION_CERTIFICATE_TRANSLATION: self.KrstatusChoices.ONGOING_GRADUATION_CERTIFICATE_TRANSLATION,
                self.EnstatusChoices.COMPLETED_NOTARIZATION_GRADUATION_CERTIFICATE_TRANSLATION: self.KrstatusChoices.COMPLETED_NOTARIZATION_GRADUATION_CERTIFICATE_TRANSLATION,
                self.EnstatusChoices.PLEASE_VISIT_POST_OFFICE: self.KrstatusChoices.PLEASE_VISIT_POST_OFFICE,
                self.EnstatusChoices.ONGOING_HOUSE_ADDRESS_REGISTRATION: self.KrstatusChoices.ONGOING_HOUSE_ADDRESS_REGISTRATION,
                self.EnstatusChoices.COMPLETED_HOUSE_ADDRESS_REGISTRATION: self.KrstatusChoices.COMPLETED_HOUSE_ADDRESS_REGISTRATION,
                self.EnstatusChoices.ANNOUNCEMENT_FIRST_VISIT_SCHEDULE: self.KrstatusChoices.ANNOUNCEMENT_FIRST_VISIT_SCHEDULE,
                self.EnstatusChoices.FIRST_VISIT: self.KrstatusChoices.FIRST_VISIT,
                self.EnstatusChoices.PLEASE_PAY_DRIVING_LICENSE_EXCHANGE_COST: self.KrstatusChoices.PLEASE_PAY_DRIVING_LICENSE_EXCHANGE_COST,
                self.EnstatusChoices.ANNOUNCEMENT_SECOND_VISIT_SCHEDULE: self.KrstatusChoices.ANNOUNCEMENT_SECOND_VISIT_SCHEDULE,
                self.EnstatusChoices.SECOND_VISIT: self.KrstatusChoices.SECOND_VISIT,
                self.EnstatusChoices.REVISIT_NEEDED: self.KrstatusChoices.REVISIT_NEEDED,
                self.EnstatusChoices.TEMPORARY_CARD: self.KrstatusChoices.TEMPORARY_CARD,
                self.EnstatusChoices.APPROVEDANDWAITFORCARD: self.KrstatusChoices.APPROVEDANDWAITFORCARD,
                self.EnstatusChoices.COMPLETED: self.KrstatusChoices.COMPLETED,
        }
        self.krstatus = mapping.get(self.enstatus, '')
        super().save(*args, **kwargs)

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


    def __str__(self):
        return "Driving license"
    
    class Meta:
        verbose_name_plural = "Driving licenses"
