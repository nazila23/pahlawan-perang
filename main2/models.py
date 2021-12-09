from django.db import models
# from django.db.models.base import Model
# from django.db.models.fields import CharField, EmailField, IntegerField
# Create your models here.
class anggota(models.Model):
    kelamin = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]

    nama = models.TextField(max_length=200)
    tanggal_lahir =models.CharField(max_length=200)
    anggota_sejak =models.CharField(max_length=200)
    tanggal_registrasi =models.CharField(max_length=200)
    berlaku_hingga =models.CharField(max_length=200)
    tipe_anggota =models.TextField(max_length=200)
    pekerjaan =models.TextField(max_length=200)
    alamat =models.TextField(max_length=200)
    jenis_kelamin =models.TextField(choices=kelamin, max_length=200)
    negara =models.TextField(max_length=200)
    no_hp =models.IntegerField(default=0)
    email =models.TextField(max_length=200)
    instansi =models.TextField(max_length=200)

class buku(models.Model):
    isi = [
        ('fiksi', 'fiksi'),
        ('pendidikan', 'pendidikan'),
    ]

    media= [
        ('cetak', 'cetak'),
        ('online', 'online'),
    ]

    opac = [
        ('tampil','tampil'),
        ('sembunyi','sembunyi'),
    ]
    judul = models.CharField(max_length=200)
    pengarang = models.CharField(max_length=200)
    edisi = models.CharField(max_length=200)
    info_detail_spesifikasi = models.CharField(max_length=200)
    tipe_isi = models.CharField(choices=isi, max_length=200)
    tipe_media = models.CharField(choices = media, max_length=200)
    isbn = models.CharField(max_length=200)
    penerbit = models.CharField(max_length=200)
    tahun_terbit = models.IntegerField()
    tempat_terbit = models.CharField(max_length=200)
    diskripsi_fisik = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=200)
    no_panggil = models.IntegerField()
    bahasa = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='cars')
    opac = models.TextField(choices=opac)
    beranda = models.TextField(max_length=200)
