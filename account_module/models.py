from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile',verbose_name='تصویر اواتار', null=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل', blank=True, editable=False)
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره ی  کاربر')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        else:
            return self.email