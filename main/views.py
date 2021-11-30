from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http.response import Http404


def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def order(request):
    return render(request,'order.html')
def dashboard(request):
    return render(request,'dashboard.html')
def tambah(request):
    return render(request,'tambah.html')
def usersprof(request):
    return render(request,'usersprof.html')
def usulan(request):
    return render(request,'usulan.html')
def upload(request):
    return render(request,'upload-karya.html')
def order(request):
    return render(request,'order-buku.html')
def bebas(request):
    return render(request,'bebas-pustaka.html')
def biblografi(request):
    return render(request,'biblografi.html')
def daftaranggota(request):
    return render(request,'daftaranggota.html')
def daftarbiblografi(request):
    return render(request,'daftarbiblografi.html')
def dataexemplar(request):
    return render(request,'dataexemplar.html')
def daftarexemplar(request):
    return render(request,'daftarexemplar.html')




