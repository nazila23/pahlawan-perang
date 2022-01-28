from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.files import File
from django.conf import settings
import PIL.Image
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.db.models import Q

class karyawan(models.Model):
    kelamin =[
        ('Laki-Laki','Laki-Laki'),
        ('Perempuan','Perempuan'),
    ]
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.DateField()
    jabatan = models.CharField(max_length=200)
    alamat = models.CharField(max_length=200)
    no_hp = models.IntegerField()
    email = models. CharField(max_length=200)
    jenis_kelamin= models.CharField(choices=kelamin, max_length=200)

class anggota(models.Model):
    kelamin = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]
    anggota = [
        ('Mahasiswa', 'Mahasiswa'),
        ('Umum', 'Umum'),
        ('Santri', 'Santri'),
    ]
    nama = models.TextField(max_length=200)
    tanggal_lahir =models.CharField(max_length=200)
    tanggal_registrasi = models.DateField(auto_now_add=True)
    berlaku_hingga =models.CharField(max_length=200)
    tipe_anggota =models.CharField(choices=anggota, max_length=200)
    pekerjaan =models.TextField(max_length=200)
    alamat =models.TextField(max_length=200)
    jenis_kelamin =models.CharField(choices=kelamin, max_length=200)
    negara =models.TextField(max_length=200)
    no_hp =models.BigIntegerField()
    email =models.TextField(max_length=200)
    instansi =models.TextField(max_length=200)
    # id_karyawan=models.ForeignKey(karyawan, on_delete=CASCADE,related_name='ak')

    
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

    beranda = [
         ('tampil','tampil'),
        ('sembunyi','sembunyi'),
    ]

    judul = models.CharField(max_length=200)
    pengarang = models.CharField(max_length=200)
    edisi = models.CharField(max_length=200)
    info_detail_spesifikasi = models.CharField(max_length=200)
    tipe_isi = models.CharField(choices=isi, max_length=200)
    tipe_media = models.CharField(choices=media, max_length=200)
    isbn = models.CharField(max_length=200)
    penerbit = models.CharField(max_length=200)
    tahun_terbit = models.IntegerField()
    tempat_terbit = models.CharField(max_length=200)
    diskripsi_fisik = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=200)
    bahasa = models.CharField(max_length=200)
    cover = models.ImageField(default='', upload_to='images/', null=True, blank=True)
    opac =models.CharField(choices=opac, max_length=200)
    beranda = models.CharField(choices=beranda, max_length=200)
    # id_karyawan=models.ForeignKey(karyawan, on_delete=CASCADE,related_name='aks')

class exemplar (models.Model):
    beranda = [
        ('tampil','tampil'),
        ('sembunyi','sembunyi'),
    ]
    kode_exemplar = models.CharField(max_length=200)
    no_panggil =  models.CharField(max_length=200)
    kode_inventaris=  models.CharField(max_length=200)
    lokasi = models.CharField(max_length=200)
    tgl_pesan = models.CharField(max_length=200)
    tgl_terima = models.CharField(max_length=200)
    promosi = models.CharField(choices=beranda, max_length=200)
    jumlah_exemplar= models.CharField(max_length=200)
    id_karyawan=models.ForeignKey(karyawan, on_delete=CASCADE,related_name='aksi')
    id_buku=models.ForeignKey(buku, on_delete=CASCADE,related_name='data')
class pinjam (models.Model):
    aksi= [
        ('Ditempat','Ditempat'),
        ('Diambil','Diambil'),
         ('Dikirim','Dikirim'),
    ]
    tgl_pinjam =models.DateField(auto_now=True)
    tgl_kembali = models.CharField(max_length=200)
    denda = models.IntegerField(null=True, blank=True)
    alamat =models.TextField(max_length=200)
    transaksi=models.CharField(choices=aksi, max_length=200)
    id_buku=models.ForeignKey(buku, on_delete=CASCADE,related_name='inputan1')
    id_karyawan=models.ForeignKey(karyawan, on_delete=CASCADE,related_name='pengisi')
    id_exemplar=models.ForeignKey(exemplar, on_delete=CASCADE,related_name='isi')
    id_anggota=models.ForeignKey(anggota, on_delete=CASCADE,related_name='value')

