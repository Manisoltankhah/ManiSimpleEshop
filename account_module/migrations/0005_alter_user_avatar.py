# Generated by Django 3.2.8 on 2022-03-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=20, null=True, verbose_name='تصویر اواتار'),
        ),
    ]
