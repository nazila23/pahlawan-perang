from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.files import File
from django.conf import settings
import PIL.Image
from django.db.models.deletion import CASCADE, DO_NOTHING

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
    tipe = [
        ('santri', 'santri'),
        ('umum', 'umum'),
    ]
    nama = models.TextField(max_length=200)
    tanggal_lahir =models.CharField(max_length=200)
    tanggal_registrasi = models.DateField(auto_now_add=True)
    berlaku_hingga =models.CharField(max_length=200)
    tipe_anggota =models.TextField(choices=tipe, max_length=200)
    pekerjaan =models.TextField(max_length=200)
    alamat =models.TextField(max_length=200)
    jenis_kelamin =models.CharField(choices=kelamin, max_length=200)
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

    # opac = [ 
    #     ('tampil','tampil'),
    #     ('sembunyi','sembunyi'),
    # ]

    beranda = [
         ('tampil','tampil'),
        ('sembunyi','sembunyi'),
    ]
    judul = models.CharField(max_length=200)
    pengarang = models.CharField(max_length=200)
    edisi = models.CharField(max_length=200)
    tipe_isi = models.CharField(choices=isi, max_length=200)
    tipe_media = models.CharField(choices=media, max_length=200)
    isbn = models.CharField(max_length=200)
    penerbit = models.CharField(max_length=200)
    tahun_terbit = models.IntegerField()
    tempat_terbit = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=200)
    bahasa = models.CharField(max_length=200)
    cover = models.ImageField(default='', upload_to='images/', null=True, blank=True)
    beranda = models.CharField(choices=beranda, max_length=200)

    def __str__(self):
        return self.judul
        
class exemplar (models.Model):
    beranda = [
        ('tampil','tampil'),
        ('sembunyi','sembunyi'),
    ]
    no_panggil= models.CharField(max_length=200)
    pengarang = models.CharField(max_length=200)
    kode_exemplar= models.CharField(max_length=200)
    kode_inventaris=  models.CharField(max_length=200)
    lokasi= models.CharField(max_length=200)
    jmlh_exemplar= models.CharField(max_length=200)
    judul = models.ForeignKey(buku, on_delete=DO_NOTHING)


class Pinjam (models.Model):
    tgl_pinjam = models.DateField(auto_now_add=True)
    tgl_kembali = models.DateField(auto_now=True)
    denda = models.CharField(max_length=200)
    no_panggil = models.ForeignKey(exemplar,on_delete=DO_NOTHING)

    def tgl_pinjam_format(self):
        return self.tgl_pinjam.strftime('%Y-%m-%d')
    def tgl_kembali_format(self):
        return self.tgl_kembali.strftime('%Y-%m-%d')
