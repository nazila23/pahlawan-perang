# Generated by Django 3.2.8 on 2022-01-13 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anggota',
            name='no_hp',
            field=models.BigIntegerField(),
        ),
    ]
