# Generated by Django 3.2.8 on 2021-12-03 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anggota',
            old_name='Berlaku_hingga',
            new_name='berlaku_hingga',
        ),
    ]
