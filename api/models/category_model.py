from django.db import models

from api.models import Merchandise, User


class Category(models.Model):
    merchandise = models.ForeignKey(
        Merchandise,
        on_delete=models.CASCADE,
        related_name="categories",
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=255,
        help_text="Name of category"
    )

    is_available = models.BooleanField(
        default=False,
    )

    on_time = models.TimeField(
        null=False,
        blank=False
    )

    off_time = models.TimeField(
        null=False,
        blank=False
    )

    additional_detail = models.TextField(
        null=True,
        blank=True,
        help_text="Any additional detail for this category"
    )

    added_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
