# Generated by Django 3.2.8 on 2022-03-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0007_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_active_code',
            field=models.CharField(blank=True, editable=False, max_length=100, verbose_name='کد فعال سازی ایمیل'),
        ),
    ]
