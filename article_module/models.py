from django.db import models
from jalali_date import date2jalali

from account_module.models import User


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, verbose_name='دسته بندی والد', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی در لینک', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندهای مقاله'


class Article(models.Model):
    title = models.CharField(max_length=500, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='عنوان در لینک')
    image = models.ImageField(upload_to='images/Articles', verbose_name='تصویر مقاله')
    short_descriptions = models.TextField(verbose_name='توضیحات')
    text = models.TextField(verbose_name='متن')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی ها')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ثبت')

    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.created_date)

    def get_jalali_create_time(self):
        return self.created_date.strftime('%H:%M')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey("ArticleComment", on_delete=models.CASCADE, verbose_name='والد', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرهای مقاله'














