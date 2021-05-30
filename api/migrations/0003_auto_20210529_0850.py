# Generated by Django 3.2.3 on 2021-05-29 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_owner_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchandise',
            name='vendor',
        ),
        migrations.AddField(
            model_name='merchandise',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='merchandise',
            name='state',
            field=models.CharField(choices=[('NOT APPROVED', 'NOT APPROVED'), ('APPROVED', 'APPROVED')], default='NOT APPROVED', max_length=100),
        ),
        migrations.AlterField(
            model_name='merchandisedocument',
            name='title',
            field=models.CharField(help_text='Type of document e.g AADHAAR, FSSAI, PAN', max_length=200),
        ),
    ]