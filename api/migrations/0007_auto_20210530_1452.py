# Generated by Django 3.2.3 on 2021-05-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_billing'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_root',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
