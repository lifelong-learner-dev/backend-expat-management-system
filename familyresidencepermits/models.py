from django.db import models
from common.models import CommonModel
from datetime import date

class Familyresidencepermit(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )

    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="familyresidencepermits",
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

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    turkish_id = models.SmallIntegerField(("Turkish ID number"), null=False, default="1",)
    tc_id_expiry_date = models.DateField(("TC expiry date"), default=date.today)
    passport_number = models.CharField(max_length=20, blank=True)
    passport_expiry_date = models.DateField(("passport expiry date"), default=date.today)

    family = models.CharField(
        max_length=10,
        choices=FamilyChoices.choices,
        blank=True,)

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        blank=True,)

    def __str__(self):
        return self.name
    


