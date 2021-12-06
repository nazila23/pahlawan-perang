# Generated by Django 3.2.8 on 2021-12-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main2', '0009_auto_20211206_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('pengarang', models.CharField(max_length=200)),
                ('edisi', models.CharField(max_length=200)),
                ('info_detail_spesifikasi', models.CharField(max_length=200)),
                ('tipe_isi', models.CharField(choices=[('fiksi', 'fiksi'), ('pendidikan', 'pendidikan')], max_length=200)),
                ('tipe_media', models.CharField(choices=[('cetak', 'cetak'), ('online', 'online')], max_length=200)),
                ('isbn', models.CharField(max_length=200)),
                ('penerbit', models.CharField(max_length=200)),
                ('tahun_terbit', models.IntegerField()),
                ('tempat_terbit', models.CharField(max_length=200)),
                ('diskripsi_fisik', models.CharField(max_length=200)),
                ('klasifikasi', models.CharField(max_length=200)),
                ('no_panggil', models.IntegerField()),
                ('bahasa', models.CharField(max_length=200)),
                ('cover', models.ImageField(upload_to='')),
                ('opac', models.TextField(choices=[('tampil', 'tampil'), ('sembunyi', 'sembunyi')])),
                ('beranda', models.TextField(max_length=200)),
            ],
        ),
    ]
