from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, EmailField, IntegerField
# Create your models here.
class anggota(models.Model):
    nama = models.TextField(max_length=200)
    tanggal_lahir =models.CharField(max_length=200)
    jenis_kelamin =models.TextField(max_length=200)
    pekerjaan =models.TextField(max_length=200)
    alamat =models.TextField(max_length=200)
    negara =models.TextField(max_length=200)
    no_hp=models.IntegerField()
    email =models.TextField(max_length=200)
    password = models.CharField(max_length=200)
    instansi =models.TextField(max_length=200)

# class buku(models.Model):
#     judul = models.TextField(max_length=200)
#     pengarang = models.TextField(max_length=200)
#     edisi = models.CharField(max_length=200)
#     terbit = models.TextField(max_length=200)
#     tempat_terbit = models.TextField(max_length=200)
#     Deskripsi_fisik = models.TextField(max_length=200)
#     judul_seri = models.TextField(max_length=200)
#     klasifikasi = models.TextField(max_length=200)
#     No_panggil = models.TextField(max_length=200)
#     Subyek = models.TextField(max_length=200)
#     bahasa = models.TextField(max_length=200)
#     gambar_sampul = models.TextField(max_length=200)
    

    
