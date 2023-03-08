from django.db import models
from common.models import CommonModel

class Process(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    responsible_person = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="processes",
        null=True,
        blank=True,
    )
    explanations = models.ManyToManyField(
        "processes.Explanation",
        related_name="processes",
    )
    documents = models.ManyToManyField(
        "processes.Document",
        related_name="processes",
    )

    def total_explanations(process):
        return process.explanations.count()
    
    def total_documents(process):
        return process.documents.count()
    
    def __str__(self):
        return "Process"
    
    class Meta:
        verbose_name_plural = "Processes"

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