from django.db import models
from common.models import CommonModel
from datetime import date, time

class Green_cards_preparation_document(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )

    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="green_cards_preparation_documents",
    )
    contents = models.CharField(
        max_length=5000,
        default="",
    )

    signing_authority = models.CharField(
        max_length=180,
        default="",
    )

    certified_translator = models.CharField(
        max_length=180,
        default="",
    )