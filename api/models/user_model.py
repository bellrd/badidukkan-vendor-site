from django.contrib.auth.models import (BaseUserManager, AbstractUser)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyUserManager(BaseUserManager):
    def create_user(self, mobile_number, password, **extra_fields):
        if not mobile_number:
            raise ValueError('The mobile number must be set')
        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.is_staff = True
        user.is_root = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, mobile_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(mobile_number, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    name = models.CharField(
        null=True,
        blank=True,
        max_length=200,
        unique=False,
        help_text="Full name of user"
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )

    mobile_number = models.CharField(
        max_length=10,
        unique=True,
        help_text="Enter mobile number without country code",
    )

    is_vendor = models.BooleanField(
        default=True,
        help_text='Only for vendor',
        verbose_name='Vendor account'
    )

    is_active = models.BooleanField(
        default=True,
        help_text='User can login?',
    )

    is_superuser = models.BooleanField(
        default=True,
    )

    is_root = models.BooleanField(
        default=False
    )


    objects = MyUserManager()
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.name) if self.name else str(self.mobile_number)  # str is required


@receiver(post_save, sender=User)
def user_created_handler(sender, instance=None, created=False, **kwargs):
    pass
    # if created:
    #     Token.objects.create(user=instance)
