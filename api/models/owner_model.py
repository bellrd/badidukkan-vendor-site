import os
from datetime import datetime
from os.path import splitext

from django.db import models
from api.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


def owner_photo_upload_handler(instance, filename):
    directory = "Images/OwnerPhotos/"
    extension = str(splitext(filename))[1]
    name = instance.name + str(datetime.now()).replace(' ', "_") + str(extension)
    return os.path.join(directory, name)


class Owner(models.Model):
    name = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        help_text="Legal Name of owner",
    )

    owner_photo = models.ImageField(
        upload_to=owner_photo_upload_handler,
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
        max_length=100,
    )

    bank_account = models.CharField(
        max_length=40,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Owner bank account number",
        help_text="This account will be used for transaction",
    )

    ifsc_code = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )

    mobile_number = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        unique=True,
        help_text="Personal mobile number"
    )

    address = models.TextField(
        verbose_name="Address of owner",
        help_text="Multiple address allowed separated by ;"
    )

    additional_detail = models.TextField(
        help_text="Additional detail of owner"
    )

    added_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


def owner_document_upload_handler(instance, filename):
    directory = "Documents/OwnerDocuments/"
    extension = str(splitext(filename))[1]
    name = str(instance.owner.name + "_" + instance.title) + str(datetime.now()) + str(extension)
    return os.path.join(directory, name.replace(' ', '_'))


class OwnerDocument(models.Model):
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        verbose_name="Type of Document",
        max_length=40,
        help_text="Enter Document type in CAPS"
    )

    file = models.FileField(
        upload_to=owner_document_upload_handler,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

