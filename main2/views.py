from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http.response import Http404
from django.db.models.base import Model
from.import models
from .models import anggota
from .models import buku
# Create your views here.

def biblografi(request):
    if request.POST:
        models.buku.objects.create(
            judul = request.POST ['Judul'],
            pengarang = request.POST ['Pengarang'],
            edisi = request.POST ['Edisi'],
            info_detail_spesifikasi = request.POST ['ids'],
            tipe_isi = request.POST ['isi'],
            tipe_media = request.POST ['media'],
            isbn = request.POST ['isbn'],
            penerbit = request.POST ['penerbit'],
            tahun_terbit = request.POST ['tpenerbit'],
            tempat_terbit = request.POST['tterbit'],
            diskripsi_fisik = request.POST ['ds'],
            klasifikasi = request.POST ['klasifikasi'],
            no_panggil = request.POST ['np'],
            bahasa = request.POST ['bhs'],
            cover = request.POST ['cover'],
            opac = request.POST ['gridRadioss'],
            beranda = request.POST ['gridRadios'],
        )
    data=models.buku.objects.all()
    return render(request,'biblografi.html',{
        'data': data,
    })
# Fungsi Anggota
def anggota(request):
    if request.POST:
        models.anggota.objects.create(
            nama = request.POST ['nama'],
            tanggal_lahir = request.POST ['tl'],
            # anggota_sejak = request.POST ['as'],
            tanggal_registrasi = request.POST ['tr'],
            berlaku_hingga = request.POST ['bg'],
            tipe_anggota = request.POST ['tk'],
            pekerjaan = request.POST ['pekerjaan'],
            alamat = request.POST ['almt'],
            negara = request.POST ['negara'],
            no_hp = request.POST['hp'],
            email = request.POST ['email'],
            instansi = request.POST ['ins'],
            jenis_kelamin = request.POST ['jenisk'],
        )
    data=models.anggota.objects.all()
    return render(request,'anggota.html',{
        'data': data,
    })

def delete_anggota(request,id):
    models.anggota.objects.filter(pk=id).delete()
    return redirect ('anggota')


def edit_anggota(request,id):
    if request.POST:
        models.anggota.objects.filter(id=id).update(
            nama = request.POST ['nama'],
            tanggal_lahir = request.POST ['tanggal_lahir'],
            # anggota_sejak = request.POST ['anggota_sejak'],
            tanggal_registrasi = request.POST ['tanggal_registrasi'],
            berlaku_hingga = request.POST ['berlaku_hingga'],
            tipe_anggota = request.POST ['tipe_anggota'],
            pekerjaan = request.POST ['pekerjaan'],
            alamat = request.POST ['alamat'],
            negara = request.POST ['negara'],
            no_hp = request.POST['no_hp'],
            email = request.POST ['email'],
            instansi = request.POST ['instansi'],
            jenis_kelamin = request.POST ['jenis_kelamin'],
        )
        return redirect('anggota')
    data = models.anggota.objects.filter(pk=id).first()
    print(data)
    return render (request, 'edit_anggota.html',{
        'data':data,
    })

def detail_anggota(request,id):
    detail = models.anggota.objects.filter(pk=id).first()
    return render (request,'detail_anggota.html', {
        'data': detail,
    })
def exemplar(request):
    return render(request,'exemplar.html')
def biodata(request):
    return render(request,'biodata.html')
def sirkulasi(request):
    return render(request,'sirkulasi.html')
def sidebarpustaka(request):
    return render(request,'sidebarpustaka.html')
def transaksi(request):
    return render(request,'transaksi.html')
def login(request):
    return render(request,'login.html')

