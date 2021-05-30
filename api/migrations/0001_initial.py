# Generated by Django 3.2.3 on 2021-05-28 14:33

import api.models.merchandise_model
import api.models.owner_model
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, help_text='Full name of user', max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('mobile_number', models.CharField(help_text='Enter mobile number without country code', max_length=10, unique=True)),
                ('is_vendor', models.BooleanField(default=True, help_text='Only for vendor', verbose_name='Vendor account')),
                ('is_active', models.BooleanField(default=True, help_text='User can login?')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of merchandise', max_length=255)),
                ('tag_line', models.CharField(blank=True, help_text='Some tagline regarding merchandise eg. (Famous for biryani/South)', max_length=256, null=True)),
                ('is_available', models.BooleanField(default=False, help_text='Is merchandise service available?')),
                ('photo_url', models.ImageField(blank=True, help_text='Main image of merchandise', null=True, upload_to=api.models.merchandise_model.merchandise_photo_upload_handler)),
                ('address', models.TextField()),
                ('additional_detail', models.TextField(blank=True, help_text='Any additional detail for merchandise', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Legal Name of owner', max_length=40)),
                ('owner_photo', models.ImageField(blank=True, null=True, upload_to=api.models.owner_model.owner_photo_upload_handler)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('bank_account', models.CharField(help_text='This account will be used for transaction', max_length=40, unique=True, verbose_name='Owner bank account number')),
                ('ifsc_code', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(help_text='Personal mobile number', max_length=40, unique=True)),
                ('address', models.TextField(help_text='Multiple address allowed separated by ;', verbose_name='Address of owner')),
                ('additional_detail', models.TextField(help_text='Additional detail of owner')),
            ],
        ),
        migrations.CreateModel(
            name='OwnerDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter Document type in CAPS', max_length=40, verbose_name='Type of Document')),
                ('file', models.FileField(blank=True, null=True, upload_to=api.models.owner_model.owner_document_upload_handler)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.owner')),
            ],
        ),
        migrations.CreateModel(
            name='MerchandiseDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Type of document e.g AADHAR, FSSAI, PAN', max_length=200)),
                ('file', models.FileField(upload_to=api.models.merchandise_model.merchandise_document_handler)),
                ('merchandise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.merchandise')),
            ],
        ),
        migrations.AddField(
            model_name='merchandise',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.owner'),
        ),
        migrations.AddField(
            model_name='merchandise',
            name='vendor',
            field=models.OneToOneField(help_text='vendor (user) to manage this merchandise', limit_choices_to={'is_vendor': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NOT APPROVED', 'NOT APPROVED'), ('APPROVED', 'APPROVED')], default='NOT APPROVED', max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('merchandise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.merchandise')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of category', max_length=255)),
                ('is_available', models.BooleanField(default=False)),
                ('on_time', models.TimeField()),
                ('off_time', models.TimeField()),
                ('additional_detail', models.TextField(blank=True, help_text='Any additional detail for this category', null=True)),
                ('merchandise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='api.merchandise')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
