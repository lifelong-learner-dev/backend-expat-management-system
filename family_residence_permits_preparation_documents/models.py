from django.db import models
from common.models import CommonModel
from datetime import date
from django.utils.timezone import now

class Family_residence_permits_preparation_document(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    expat_name = models.CharField(
        max_length=180,
        default="",
    )
    expat_birth_date = models.DateField(("Expat birth date"), default=date.today)

    expat_id_number = models.CharField(
        max_length=15,
        default="",
    )
    expat_gender = models.CharField(
        max_length=15,
        default="",
    )

    spouse_name = models.CharField(
        max_length=180,
        default="",
    )
    spouse_birth_date = models.DateField(("Spouse birth date"), default=date.today)

    spouse_id = models.CharField(
        max_length=15,
        default="",
    )
    spouse_gender = models.CharField(
        max_length=15,
        default="",
    )
    do_you_have_children = models.BooleanField(default=False)

    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="family_residence_permits_preparation_documents",
    )
    residence_permit = models.ForeignKey(
        "family_residence_permits.Family_residence_permit",
        on_delete=models.CASCADE,
        related_name="family_residence_permits_preparation_documents",
    )

    class EndocumentsChoices(models.TextChoices):
        POWER_OF_ATTORNEY = ("power_of_attorney", "Power of attorney")
        COORPERATION_LETTER = ("cooperation_letter", "Cooperation letter")
        EXPAT_FAMILY_RELATIONS_CERTIFICATE = ("expat_family_relations_certificate", "Expat Family relations certificate")
        SPOUSE_FAMILY_RELATIONS_CERTIFICATE = ("spouse_family_relations_certificate", "Spouse Family relations certificate")
        CHILD1_FAMILY_RELATIONS_CERTIFICATE = ("child1_family_relations_certificate", "Child1 Family relations certificate")
        CHILD2_FAMILY_RELATIONS_CERTIFICATE = ("child2_family_relations_certificate", "Child2 Family relations certificate")
        CHILD3_FAMILY_RELATIONS_CERTIFICATE = ("child3_family_relations_certificate", "Child3 Family relations certificate")
        CHILD4_FAMILY_RELATIONS_CERTIFICATE = ("child4_family_relations_certificate", "Child4 Family relations certificate")
        CRIMINAL_RECORD_CERTIFICATE = ("criminal_record_certificate", "Criminal record certificate")
        NATIONAL_POLICE_SERVICE = ("national_police_service", "National police service")
        MARRIAGE_CERTIFICATE = ("marriage_certificate", "Marriage certificate")
        
    endocument = models.CharField(
        max_length=150,
        choices=EndocumentsChoices.choices,
        blank=True,)
        
    marriage_certificate_address = models.CharField(
        max_length=1000,
        default="",
        blank=True,
    )
    marriage_certificate_marriage_date = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    marriage_certificate_approved_date = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    marriage_certificate_approved_person = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    marriage_certificate_approved_place = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    marriage_certificate_document_date = models.DateField(("Document date of Marriage certificate"), default=date.today, blank=True,)
    marriage_certificate_document_public_office = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    marriage_certificate_authorized_person = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    marriage_certificate_document_time = models.TimeField(("Document time of Marriage certificate"), default="19:00", blank=True,)
    marriage_certificate_responsible_person = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    marriage_certificate_cellphone_number = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    marriage_certificate_person_who_request = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    marriage_certificate_document_number = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    
    criminal_record_address = models.CharField(
        max_length=1000,
        default="",
        blank=True,
    )

    criminal_record_document_date = models.DateField(("Document date of Criminal record certificate"), default=date.today, blank=True,)

    criminal_record_document_date_time = models.DateTimeField(("Document time of Criminal record certificate"), default=now, blank=True,)

    criminal_record_person_who_request = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    criminal_record_document_number = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    child_name = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_birth_date = models.DateField(("Child birth date"), default=date.today,blank=True,)

    child_id = models.CharField(
        max_length=15,
        default="",
        blank=True,
    )
    child_gender = models.CharField(
        max_length=15,
        default="",
        blank=True,
    )
    
    child_family_relations_certificate_address = models.CharField(
        max_length=1000,
        default="",
        blank=True,
    )
 
    child_family_relations_certificate_document_date = models.DateField(("Document date of child family relations certificate"), default=date.today, blank=True,)
    child_family_relations_certificate_document_public_office = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_authorized_person = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_document_time = models.TimeField(("Document time of child family relations certificate"), default="19:00", blank=True,)
    child_family_relations_certificate_responsible_person = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_cellphone_number = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_person_who_request = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    child_family_relations_certificate_consulate_date = models.DateField(("Document date of Consulate"), default=date.today, blank=True,)
    child_family_relations_certificate_document_number = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    child_name2 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_birth_date2 = models.DateField(("Child birth date"), default=date.today,blank=True,)

    child_id2 = models.CharField(
        max_length=15,
        default="",
        blank=True,
    )
    child_gender2 = models.CharField(
        max_length=15,
        default="",
        blank=True,
    )
    
    child_family_relations_certificate_address2 = models.CharField(
        max_length=1000,
        default="",
        blank=True,
    )
 
    child_family_relations_certificate_document_date2 = models.DateField(("Document date of child family relations certificate"), default=date.today, blank=True,)
    child_family_relations_certificate_document_public_office2 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_authorized_person2 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_document_time2 = models.TimeField(("Document time of child family relations certificate"), default="19:00", blank=True,)
    child_family_relations_certificate_responsible_person2 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_cellphone_number2 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_person_who_request2 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    child_family_relations_certificate_consulate_date2 = models.DateField(("Document date of Consulate"), default=date.today, blank=True,)
    child_family_relations_certificate_document_number2 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    child_name3 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_birth_date3 = models.DateField(("Child birth date"), default=date.today,blank=True,)

    child_id3 = models.CharField(
        max_length=15,
        default="",
        blank=True,
    )
    child_gender3 = models.CharField(
        max_length=15,
        default="",
        blank=True,
    )
    
    child_family_relations_certificate_address3 = models.CharField(
        max_length=1000,
        default="",
        blank=True,
    )
 
    child_family_relations_certificate_document_date3 = models.DateField(("Document date of child family relations certificate"), default=date.today, blank=True,)
    child_family_relations_certificate_document_public_office3 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_authorized_person3 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_document_time3 = models.TimeField(("Document time of child family relations certificate"), default="19:00", blank=True,)
    child_family_relations_certificate_responsible_person3 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_cellphone_number3 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_person_who_request3 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    child_family_relations_certificate_consulate_date3 = models.DateField(("Document date of Consulate"), default=date.today, blank=True,)
    child_family_relations_certificate_document_number3 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    child_name4 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_birth_date4 = models.DateField(("Child birth date"), default=date.today,blank=True,)

    child_id4 = models.CharField(
        max_length=15,
        default="",
        blank=True,
    )
    child_gender4 = models.CharField(
        max_length=15,
        default="",
        blank=True,
    )
    
    child_family_relations_certificate_address4 = models.CharField(
        max_length=1000,
        default="",
        blank=True,
    )
 
    child_family_relations_certificate_document_date4 = models.DateField(("Document date of child family relations certificate"), default=date.today, blank=True,)
    child_family_relations_certificate_document_public_office4 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_authorized_person4 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_document_time4 = models.TimeField(("Document time of child family relations certificate"), default="19:00", blank=True,)
    child_family_relations_certificate_responsible_person4 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_cellphone_number4 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    child_family_relations_certificate_person_who_request4 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    child_family_relations_certificate_consulate_date4 = models.DateField(("Document date of Consulate"), default=date.today, blank=True,)
    child_family_relations_certificate_document_number4 = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    national_police_service_address = models.CharField(
        max_length=1000,
        default="",
        blank=True,
    )

    national_police_service_document_result = models.DateField(("Document result date of National police service certificate"), default=date.today, blank=True,)
    national_police_service_consulate_result = models.DateField(("consulate result date of National police service certificate"), default=date.today, blank=True,)

    national_police_service_official = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    national_police_service_authorized_official = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )
    national_police_service_document_number = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    def __str__(self):
        return "Family residence permit preparation document"
    
    class Meta:
        verbose_name_plural = "Family residence permit preparation documents"