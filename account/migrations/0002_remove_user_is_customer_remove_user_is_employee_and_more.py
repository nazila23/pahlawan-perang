# Generated by Django 4.0 on 2021-12-28 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='user',
            name='is_pemustaka',
            field=models.BooleanField(default=False, verbose_name='Is pemustaka'),
        ),
    ]
