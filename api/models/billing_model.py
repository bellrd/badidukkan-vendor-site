from django.db import models
from api.models import Merchandise

payment_status = (
    ('UNPAID', 'UNPAID'),
    ('PAID', 'PAID')
)


class Billing(models.Model):
    merchandise = models.ForeignKey(
        Merchandise,
        on_delete=models.CASCADE
    )

    amount = models.PositiveIntegerField(
        default=0
    )

    status = models.CharField(
        choices=payment_status,
        default="UNPAID",
        max_length=100
    )

    payment_link = models.CharField(
        default="",
        null=False,
        blank=False,
        max_length=256
    )

    def __str__(self):
        return self.merchandise.name
