from django.db import models
from common.models import CommonModel
from datetime import date, time

class Moving_request(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="moving_requests",
    )
    arrival_location = models.CharField(
        max_length=180,
        default="",
    )

    pre_survey_date = models.DateField(("Pre survey date"), default=date.today)
    pre_survey_time = models.TimeField(("Pre survey time"), default="19:00")

    moving_start_date = models.DateField(("Moving start date(Packing)"), default=date.today)
    moving_start_time = models.TimeField(("Moving start time"), default="19:00")

    moving_finish_date = models.DateField(("Moving finish date"), default=date.today)

    class KrreceiverChoices(models.TextChoices):
        EXPAT = ("expat", "주재원")
        SPOUSE = ("spouse", "배우자")

    class EnreceiverChoices(models.TextChoices):
        EXPAT = ("expat", "Expat")
        SPOUSE = ("spouse", "Spouse")

    class KrsituationsChoices(models.TextChoices):
        DOMESTIC = ("domestic", "국내")
        OVERSEAS = ("overseas", "해외")

    class EnsituationsChoices(models.TextChoices):
        DOMESTIC = ("domestic", "Domestic")
        OVERSEAS = ("overseas", "Overseas")

    class KrstatusChoices(models.TextChoices):
        REQUEST_SUBMITTED = ("request_submitted", "요청 제출됨")
        CHECKED = ("checked", "총무팀 확인")
        ARRANGED = ("arranged", "이사업체 및 일정 어레인지 됨")

    class EnstatusChoices(models.TextChoices):
        REQUEST_SUBMITTED = ("request_submitted", "request submitted")
        CHECKED = ("checked", "GA team checked the request")
        ARRANGED = ("arranged", "Moving company and schedule arranged")

    krsituation = models.CharField(
        max_length=150,
        choices=KrsituationsChoices.choices,
        blank=True,)

    ensituation = models.CharField(
        max_length=150,
        choices=EnsituationsChoices.choices,
        blank=True,)

    def save(self, *args, **kwargs):
        mapping = {
                self.EnsituationsChoices.DOMESTIC: self.KrsituationsChoices.DOMESTIC,
                self.EnsituationsChoices.OVERSEAS: self.KrsituationsChoices.OVERSEAS,
        }
        self.krsituation = mapping.get(self.ensituation, '')
        super().save(*args, **kwargs)

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
                self.EnstatusChoices.REQUEST_SUBMITTED: self.KrstatusChoices.REQUEST_SUBMITTED,
                self.EnstatusChoices.CHECKED: self.KrstatusChoices.CHECKED,
                self.EnstatusChoices.ARRANGED: self.KrstatusChoices.ARRANGED,
        }
        self.krstatus = mapping.get(self.enstatus, '')
        super().save(*args, **kwargs)

    krreceiver = models.CharField(
        max_length=150,
        choices=KrreceiverChoices.choices,
        blank=True,)

    enreceiver = models.CharField(
        max_length=150,
        choices=EnreceiverChoices.choices,
        blank=True,)

    def save(self, *args, **kwargs):
        mapping = {
                self.EnreceiverChoices.EXPAT: self.KrreceiverChoices.EXPAT,
                self.EnreceiverChoices.SPOUSE: self.KrreceiverChoices.SPOUSE,
        }
        self.krreceiver = mapping.get(self.enreceiver, '')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Moving requests"