from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت ')
    address = models.CharField(max_length=200, verbose_name='ادرس')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن')
    fax = models.CharField(max_length=200, null=True, blank=True,  verbose_name='فکس')
    email = models.CharField(max_length=200, null=True, blank=True,  verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='کپی رایت')
    about_us_text = models.TextField(verbose_name='درباره ما')
    site_logo = models.ImageField(upload_to='images/site_setting/', verbose_name='لوگو')
    is_main_setting = models.BooleanField('تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات اسلایدر')
    url = models.URLField(max_length=1000, verbose_name='لینک')
    url_title = models.CharField(max_length=500, verbose_name='عنوان لینک')
    is_active = models.BooleanField(default=True, verbose_name='فعال؟')
    image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایذر ها'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):

    class SiteBannerPositions(models.TextChoices):
        product_list = 'product_list', 'صفحه لیست محصولات'
        product_detail = 'product_detail', 'صفحه جزییات محصولات'
        about_us = 'about_us', 'درباره ما'

    title = models.CharField(max_length=200, verbose_name='عنوان بنر')
    url = models.URLField(max_length=400, null=True, blank=True, verbose_name='آدرس بنر')
    image = models.ImageField(upload_to='images/banners', verbose_name='عکس بنر')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    position = models.CharField(max_length=200, choices=SiteBannerPositions.choices, verbose_name='جایگاه نمایشی')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنر های تبلیغاتی'















