from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, EmailField, IntegerField
# Create your models here.
class anggota(models.Model):
    nama = models.TextField(max_length=200)
    ttl =models.CharField(max_length=200)
    sejak =models.TextField(max_length=200)
    tgl_registrasi =models.TextField(max_length=200)
    institusi =models.IntegerField()
    tipe_anggota =models.TextField(max_length=200)
    jenis_kelamin =models.TextField(max_length=200)
    alamat =models.TextField(max_length=200)
    kode_pos =models.IntegerField()
    no_tlpn =models.IntegerField()
    fax =models.IntegerField()
    Email =models.TextField(max_length=200)

class buku(models.Model):
    judul = models.TextField(max_length=200)
    pengarang = models.TextField(max_length=200)
    edisi = models.CharField(max_length=200)
    terbit = models.TextField(max_length=200)
    tempat_terbit = models.TextField(max_length=200)
    Deskripsi_fisik = models.TextField(max_length=200)
    judul_seri = models.TextField(max_length=200)
    klasifikasi = models.TextField(max_length=200)
    No_panggil = models.TextField(max_length=200)
    Subyek = models.TextField(max_length=200)
    bahasa = models.TextField(max_length=200)
    gambar_sampul = models.TextField(max_length=200)
    

    
