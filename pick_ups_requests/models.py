from django.db import models
from common.models import CommonModel
from datetime import date, time

class Pick_ups_request(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="pick_ups_requests",
    )
    will_driver_pick_you_up_from_house = models.BooleanField(default=False)

    location = models.CharField(
        max_length=180,
        default="",
    )

    date = models.DateField(("Flight date"), default=date.today)
    time = models.TimeField(("Arrival or departure time"), default="19:00")

    class DriversChoices(models.TextChoices):
        ERHAN_BEY = ("erhan_bey", "Erhan bey")
        SABRI_BEY = ("sabri_bey", "Sabri bey")
        GOKMEN_BEY = ("gokmen_bey", "Gökmen bey")

    class VehiclesChoices(models.TextChoices):
        H350_VIP = ("h350_vip", "H350 VIP")
        H350_VAN = ("h350_van", "H350 VAN")

    class KrsituationsChoices(models.TextChoices):
        FIRSTVISIT = ("familyfirstvisit", "가족 튀르키예 첫 입국")
        LASTEXIT = ("familylastexit", "가족 튀르키예 마지막 출국")

    class EnsituationsChoices(models.TextChoices):
        FIRSTVISIT = ("familyfirstvisit", "family first visit")
        LASTEXIT = ("familylastexit", "family last exit")

    class KrstatusChoices(models.TextChoices):
        REQUEST_SUBMITTED = ("request_submitted", "요청 제출됨")
        CHECKED = ("checked", "총무팀 확인")
        ARRANGED = ("arranged", "드라이버, 차량 어레인지 됨")

    class EnstatusChoices(models.TextChoices):
        REQUEST_SUBMITTED = ("request_submitted", "request submitted")
        CHECKED = ("checked", "GA team checked the request")
        ARRANGED = ("arranged", "Driver and vehicle arranged")

    driver = models.CharField(
        max_length=10,
        choices=DriversChoices.choices,
        blank=True,)

    vehicle = models.CharField(
        max_length=10,
        choices=VehiclesChoices.choices,
        blank=True,)

    krsituation = models.CharField(
        max_length=150,
        choices=KrsituationsChoices.choices,
        blank=True,)

    ensituation = models.CharField(
        max_length=150,
        choices=EnsituationsChoices.choices,
        blank=True,)

    krstatus = models.CharField(
        max_length=150,
        choices=KrstatusChoices.choices,
        blank=True,)

    enstatus = models.CharField(
        max_length=150,
        choices=EnstatusChoices.choices,
        blank=True,)