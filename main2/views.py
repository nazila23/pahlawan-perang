from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http.response import Http404
from django.db.models.base import Model
# Create your views here.

def biblografi(request):
    return render(request,'biblografi.html')
def daftarbiblografi(request):
    return render(request,'daftarbiblografi.html')
def daftaranggota(request):
    return render(request,'daftaranggota.html')
def dataexemplar(request):
    return render(request,'daftarexsemplar.html')