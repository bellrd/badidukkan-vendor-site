import os
from datetime import datetime
from os.path import splitext

from django.db import models

from api.models import Category


def item_photo_upload_handler(instance, filename):
    directory = "Images/ItemPhotos/"
    extension = str(splitext(filename))[1]
    name = instance.name + str(datetime.now()).replace(' ', "_") + str(extension)
    return os.path.join(directory, name)


class Item(models.Model):
    name = models.CharField(
        max_length=255,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="items",
    )

    photo_url = models.ImageField(
        null=True,
        blank=True,
        upload_to=item_photo_upload_handler,
        help_text="Image of item"
    )

    is_available = models.BooleanField(
        default=False
    )

    additional_detail = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Price(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="prices"
    )
    name = models.CharField(
        max_length=255,
        help_text="Size"
    )

    mrp = models.PositiveIntegerField(
        default=1,
        # max_digits=10,
        # decimal_places=2,
        help_text="MRP (price)"
    )

    additional_detail = models.CharField(
        max_length=100,
        help_text="Any description of size (max 50 letter)"
    )

    def __str__(self):
        return self.name + "@" + str(self.mrp)


class Tag(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="tags"
    )
    name = models.CharField(
        max_length=100,
        help_text="Name of tag Like VEG, NON-VEG, LOW-FAT, CARBS "
    )
    description = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="for eg. Veg item/ Non veg item/ Low fat food etc"
    )

    def __str__(self):
        return self.name
