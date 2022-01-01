from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, EmailField, IntegerField
from main2.models import anggota

class usulan(models.Model):
    judul =models.CharField(max_length=200)
    pengarang =models.CharField(max_length=200)
    tahun_terbit = models.DateField(auto_now_add=True)
    penerbit =models.CharField(max_length=200)


    

    
