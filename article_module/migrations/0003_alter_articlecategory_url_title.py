# Generated by Django 3.2.8 on 2022-03-22 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0002_auto_20220322_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='url_title',
            field=models.CharField(max_length=200, unique=True, verbose_name='عنوان دسته بندی در لینک'),
        ),
    ]
