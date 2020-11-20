from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

from .manager import *

class User(AbstractBaseUser):
    # جدید
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) 
    superuser = models.BooleanField(default=False) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # به صورت پیش فرض ایمیل و رمز ورود اجباری هستند

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):        
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_active(self):
        return self.active



# class User(AbstractUser):
#     email = models.EmailField(
#         verbose_name=_('email address'),
#         max_length=255,
#         unique=True,
#     )

#     # username = None  #  حذف فیلد نام کاربری
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [] # به صورت پیش فرض ایمیل و رمز ورود اجباری هستند

#     objects = UserManager()

#     def __str__(self):
#         return self.email