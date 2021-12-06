from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http.response import Http404
from django.db.models.base import Model
# Create your views here.

def biblografi(request):
    return render(request,'biblografi.html')
def anggota(request):
    return render(request,'anggota.html')
def exemplar(request):
    return render(request,'exemplar.html')
def biodata(request):
    return render(request,'biodata.html')
def sirkulasi(request):
    return render(request,'sirkulasi.html')