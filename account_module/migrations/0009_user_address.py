# Generated by Django 3.2.8 on 2022-07-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0008_alter_user_email_active_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
    ]