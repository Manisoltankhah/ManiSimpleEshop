from django.db import models

# Create your models here.

class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='متن')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    reponse = models.TextField(null=True, blank=True, verbose_name='پاسخ')
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده/نشده' ,default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست نماس با ما'

class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')