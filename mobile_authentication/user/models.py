from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible

from .manager import UserManager


@deconstructible
class MobileNumberValidator(RegexValidator):

    regex = r"^[0][9]\d{9}$" # یک ریجکس برای چک کردن اطلاعات ورودی کاربر

    message = _(
        'Enter a valid mobile number. This value may contain only numbers.'
    )
    flags = 0

mobile_number_validation = MobileNumberValidator() # ساخت یک اینستنس از کلاس


class User(AbstractUser):
    mobile_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name=_('Mobile Number'),
        validators=[mobile_number_validation], # جدید
        error_messages={
            'unique': _("A user with that mobile number already exists."),
        },
        help_text=_('Example') + " : 09125573688")

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.mobile_number


