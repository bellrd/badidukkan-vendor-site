import os
from datetime import datetime
from os.path import splitext

from django.db import models

from api.models import Owner, User


def merchandise_photo_upload_handler(instance, filename):
    directory = "Images/MerchandisePhotos/"
    extension = str(splitext(filename))[1]
    name = instance.name + str(datetime.now()).replace(' ', "_") + str(extension)
    return os.path.join(directory, name)


merchandise_state = (
    ('NOT APPROVED', 'NOT APPROVED'),
    ('APPROVED', 'APPROVED')
)


class Merchandise(models.Model):
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=255,
        help_text="Name of merchandise"
    )

    tag_line = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Some tagline regarding merchandise eg. (Famous for biryani/South)"
    )

    is_available = models.BooleanField(
        default=False,
        help_text="Is merchandise service available?"
    )

    photo_url = models.ImageField(
        null=True,
        blank=True,
        upload_to=merchandise_photo_upload_handler,
        help_text="Main image of merchandise"
    )

    address = models.TextField(
        null=False,
        blank=False
    )

    additional_detail = models.TextField(
        null=True,
        blank=True,
        help_text="Any additional detail for merchandise"
    )

    added_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    state = models.CharField(
        choices=merchandise_state,
        max_length=100,
        default='NOT APPROVED'
    )

    def __str__(self):
        return self.name


def merchandise_document_handler(instance, filename):
    directory = "Documents/MerchandiseDocuments/" + instance.merchandise.name
    extension = filename.split(".")[-1]
    name = instance.title + str(datetime.now()).replace(' ', "_") + "." + str(extension)
    return os.path.join(directory, name.replace(" ", ""))


class MerchandiseDocument(models.Model):
    merchandise = models.ForeignKey(
        Merchandise,
        null=True,
        on_delete=models.SET_NULL
    )

    title = models.CharField(
        max_length=200,
        help_text="Type of document e.g AADHAAR, FSSAI, PAN"
    )

    file = models.FileField(
        upload_to=merchandise_document_handler,
    )
