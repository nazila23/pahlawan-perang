from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, EmailField, IntegerField
from main2.models import anggota

# Create your models here.
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
class usulan(models.Model):
    nama = models.TextField(max_length=200)
    email =models.CharField(max_length=200)
    judul =models.CharField(max_length=200)
    pengarang =models.CharField(max_length=200)
    tahun_terbit = models.DateField(auto_now_add=True)
    penerbit =models.CharField(max_length=200)
    isbn =models.CharField(max_length=200)
    harga =models.CharField(max_length=200)

class usersprof (models.Model):
    nama = models.TextField(max_length=200)
    instansi =models.CharField(max_length=200)
    pekerjaan =models.CharField(max_length=200)
    negara =models.CharField(max_length=200)
    alamat = models.DateField(auto_now_add=True)
    no_hp =models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    pasword =models.CharField(max_length=200)
    

    
