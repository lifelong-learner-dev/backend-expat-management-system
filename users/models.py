from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        TR = ("tr", "Turkish")
        EN = ("en", "English")

    class currencyChoices(models.TextChoices):
        USD = ("usd", "USD")
        TL = ("tl", "TL")
        WON = ("won", "WON") 

    class companycarChoices(models.TextChoices):
        GENESIS = ("genesis", "GENESIS")
        SANTAFE = ("santafe", "SANTAFE")
        TUCSON = ("tucson", "TUCSON")
        ELANTRA = ("elantra","ELANTRA")

    class departmentChoices(models.TextChoices):
        GA = ("ga", "GA")
        HR = ("hr", "HR")
        PR = ("pr", "PR")
        ER = ("er", "ER")
        IT = ("it", "IT")
        FINANCE = ("finance", "FINANCE")
        SALES = ("sales", "SALES")
        AFTERSALES = ("aftersales", "AFTERSALES")
        IMPORT = ("import", "IMPORT")
        EXPORT = ("export", "EXPORT")
        AUDIT = ("audit", "AUDIT")
        PRESS = ("press", "PRESS")
        BODY = ("body", "BODY")
        PAINT = ("paint", "PAINT")
        ASSEMBLY = ("assembly", "ASSEMBLY")
        QUALITY = ("quality", "QUALITY")
        PROCUREMENT = ("procurement", "PROCUREMENT")
        

    class divisionChoices(models.TextChoices):
        CEO = ("ceo", "CEO")
        SALES = ("sales", "SALES")
        FINANCE = ("finance", "FINANCE")
        ADMIN = ("admin", "ADMIN")
        PRODUCTION = ("production", "PRODUCTION")
        PROCUREMENT = ("procurement", "PROCUREMENT")


    class positionChoices(models.TextChoices):
        CEO = ("ceo", "CEO")
        DIRECTOR = ("director", "DIRECTOR")
        COORDINATOR = ("coordinator", "COORDINATOR")

    class hqpositionChoices(models.TextChoices):
        SJ = ("sj", "SJ")
        BSJ = ("bsj", "BSJ")
        JM = ("jm", "JM")
        SM = ("sm", "SM")
        CM = ("cm", "CM")

    avatar = models.ImageField(blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_manager = models.BooleanField(default=False)
    is_expat = models.BooleanField(default=False)
    is_director = models.BooleanField(default=False)
    is_supporter = models.BooleanField(default=False)
    cellphone_number = models.SmallIntegerField(("Cellphone number"), null=False, default="1",)
    email = models.EmailField(("email address"), blank=True)
    house_address = models.CharField(max_length=150, blank=True)
    turkish_id = models.SmallIntegerField(("Turkish ID number"), null=False, default="1",)
    tc_id_expiry_date = models.DateField(("TC expiry date"), default=date.today)
    passport_number = models.CharField(max_length=20, blank=True)
    passport_expiry_date = models.DateField(("passport expiry date"), default=date.today)
    car_plate = models.CharField(max_length=20, blank=True)
    company_car_model = models.CharField(
        max_length=10,
        choices=companycarChoices.choices,
        blank=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        blank=True,
    )

    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        blank=True,
    )

    currency = models.CharField(
        max_length=5,
        choices=currencyChoices.choices,
        blank=True,
    )

    department = models.CharField(
        max_length=15,
        choices=departmentChoices.choices,
        blank=True,
    )

    division = models.CharField(
        max_length=15,
        choices=divisionChoices.choices,
        blank=True,
    )

    position = models.CharField(
        max_length=15,
        choices=positionChoices.choices,
        blank=True,
    )

    hq_position = models.CharField(
        max_length=5,
        choices=hqpositionChoices.choices,
        blank=True,
    )