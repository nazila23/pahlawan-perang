from msilib.schema import File
from statistics import mode
from django.contrib import messages
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.http.response import Http404
from django.db.models.base import Model
from . import models
from django.db.models import Q
from datetime import date, datetime
# Create your views here. 

#Fungsi Biblografi
def biblografi(request):
    if request.POST:
        models.buku.objects.create(
            judul = request.POST ['Judul'],
            pengarang = request.POST ['Pengarang'],
            edisi = request.POST ['Edisi'],
            tipe_isi = request.POST ['isi'],
            tipe_media = request.POST ['media'],
            isbn = request.POST ['isbn'],
            penerbit = request.POST ['penerbit'],
            tahun_terbit = request.POST ['tpenerbit'],
            tempat_terbit = request.POST['tterbit'],  
            klasifikasi = request.POST ['klasifikasi'],           
            bahasa = request.POST ['bhs'],
            cover = request.FILES ['cover'],
            beranda = request.POST ['gridRadioss'],
        )

       
    cari_data = models.anggota.objects.all()
    data=models.buku.objects.all()
    return render(request,'biblografi.html',{
        'data': data,
        'datanama' : cari_data,

    })

    
def delete_biblografi(request,id):
    models.buku.objects.filter(pk=id).delete()
    messages.success(request, f'Hapus Berhasil')
    return redirect ('biblografi')

def edit_biblografi(request,id):
    if request.POST:
        models.buku.objects.filter(id=id).update(
            judul = request.POST['judul'],
            pengarang = request.POST['pengarang'],
            edisi = request.POST['edisi'],
            tipe_isi = request.POST['tipe_isi'],
            tipe_media = request.POST['tipe_media'],
            isbn = request.POST['isbn'],
            penerbit = request.POST['penerbit'],
            tahun_terbit = request.POST['tahun_terbit'],
            tempat_terbit = request.POST['tempat_terbit'],
            klasifikasi = request.POST['klasifikasi'],
            bahasa = request.POST['bahasa'],
            cover = request.POST['cover'],
            beranda = request.POST['beranda'],
        )
        return redirect('biblografi')
    messages.success(request, f'Edit Berhasil')
    data = models.buku.objects.filter(pk=id).first()
    print(data)
    return render (request, 'edit_biblografi.html',{
        'data':data,

    })

def detail_biblografi(request,id):
    detail = models.buku.objects.filter(pk=id).first()
    return render (request,'detail_biblografi.html', {
        'data': detail,
    })


# Fungsi Anggota
def anggota(request):
    if request.POST:
        models.anggota.objects.create(
            nama = request.POST['nama'],
            tanggal_lahir = request.POST['tl'],
             jenis_kelamin = request.POST['jenis_kelamin'],
            tanggal_registrasi = request.POST['tr'],
            berlaku_hingga = request.POST['bg'],
            tipe_anggota = request.POST['tk'],
            pekerjaan = request.POST['pekerjaan'],
            alamat = request.POST['almt'],
            no_hp = request.POST['hp'],
            email = request.POST['email'],
            instansi = request.POST['ins'],
        )
        messages.success(request, f'Tambah Berhasil')
    data = models.anggota.objects.all()
    return render(request,'anggota.html',{
        'data': data,
    })

def delete_anggota(request,id):
    models.anggota.objects.filter(pk=id).delete()
    messages.success(request, f'Hapus Berhasil')
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
            no_hp = request.POST['no_hp'],
            email = request.POST ['email'],
            instansi = request.POST ['instansi'],
            jenis_kelamin = request.POST ['jenis_kelamin'],
        )
        return redirect('anggota')
    messages.success(request, f'Edit Berhasil')
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

#Exeemplar
def exemplar(request):
    buku= models.buku.objects.all()
    if request.POST:
        test =request.POST['judul']
        judul= models.buku.objects.get(judul=test)
        # peng=models.buku.objects.filter(pk=request.POST.get('pengarang'))
        # judul = models.buku.objects.get(pk=judul_id)
        models.exemplar.objects.create(
            judul = judul,
            pengarang = judul.pengarang,
            kode_exemplar = request.POST['k_exemplar'],
            no_panggil = request.POST['no_panggil'],
            kode_inventaris = request.POST['k_inventaris'],
            lokasi = request.POST['lokasi'],
        )
    data = models.exemplar.objects.all()
    # print(buku)
    return render(request,'exemplar.html',{
        'data': data,
        'buku': buku,

    })

def detail_exemplar(request,id):
    detail = models.exemplar.objects.filter(pk=id).first()
    return render (request,'detail_exemplar.html', {
        'data': detail,
    })

def delete_exemplar(request,id):
    models.exemplar.objects.filter(pk=id).delete()
    messages.success(request, f'Hapus Berhasil')
    return redirect ('exemplar')

def edit_exemplar(request,id):
    if request.POST:
        models.exemplar.objects.filter(id=id).update(
            judul = request.POST ['Judul'],
            pengarang = request.POST ['Pengarang'],
            kode_exemplar = request.POST ['k_exemplar'],
            no_panggil = request.POST ['no_panggil'],
            kode_inventaris = request.POST ['k_inventaris'],
            lokasi = request.POST ['lokasi'],
            # exemplar = request.POST ['exemplar'],
            # kode_pemesanan = request.POST ['kode_pemesanan'],
            tgl_pesan = request.POST['t_pemesanan'],
            tgl_terima = request.POST['t_penerima'],
            promosi = request.POST['gridRadios'],
        )
        return redirect('exemplar')
    messages.success(request, f'Edit Berhasil')
    data = models.exemplar.objects.filter(pk=id).first()
    print(data)
    return render (request,'edit_exemplar.html',{
        'data':data,
        
    })

def biodata(request):
    return render(request,'biodata.html')

def sirkulasi(request):
    if request.POST:
        input_id=request.POST['pilih']
        print (input_id)
        filter_data = models.anggota.objects.filter(pk=input_id).first()
        data=models.anggota.objects.all()
        return render(request,'sirkulasi.html',{
        'data': data,
        "filter_data": filter_data
    })
    data=models.anggota.objects.all()
    return render(request,'sirkulasi.html',{
        'data': data,
    })
    

def peminjaman(request,id):
    no_panggil= models.exemplar.objects.all()
    if request.POST:
        bakul=models.exemplar.objects.get(no_panggil=request.POST['no_panggil'])
        models.Pinjam.objects.create(
        # no_panggil=bakul,
        # judul=bakul.judul,
        tgl_pinjam=request.POST['tp'],
        tgl_kembali=request.POST['tk'],
    )
    
        # models.pinjam.objects.create(
        #     no_pang=bakul,
        #     tgl_pinjam=request.POST['tp'],
        #     tgl_kembali=request.POST['tk'],
        #     judul=request.POST['judul']
        # )
        # return redirect(request,'peminjaman.html')
    data_pinjaman=models.Pinjam.objects.filter(no_panggil=id)
    print(data_pinjaman)
    data = models.anggota.objects.filter(id=id).first()
    print(data)
    buku= models.exemplar.objects.all()
    return render(request,'peminjaman.html',{
        'data' :data,
        'data_pinjaman': data_pinjaman,
        'buku': buku,
})

# def days_between(d1,d2):
#     d1 = datetime.strptime(d1,"%y-%m-%d")
#     d2 = datetime.strptime(d2,"%y-%m-%d" )
#     return  redirect (abs((d2-d1).days),'peminjaman')

# if abs > 3:
#     denda = abs * 2000
# else :
#     denda = abs * 0
   
def exemp(request):
    cari_data = models.buku.objects.all()
    return render(request, 'exemplar.html', {
        'datanama' : cari_data
    })



def delete_pinjam(request,id):
    models.pinjam.objects.filter(pk=id).delete()
    messages.success(request, f'Hapus Berhasil')
    return redirect ('peminjaman')

def sidebarpustaka(request):
    return render(request,'sidebarpustaka.html')
    
def transaksi(request):
    return render(request,'transaksi.html')
def login(request):
    return render(request,'login.html')

def cek(request):
    cari_data = models.anggota.objects.all()
    return render(request, 'cek.html', {
        'datanama' : cari_data
    })
# def (request):
#     cari_data = models.anggota.objects.all()
#     return render(request, 'cek.html', {
#         'datanama' : cari_data
#     })

def delete_cek(request,id):
    models.anggota.objects.filter(pk=id).delete()
    messages.success(request, f'Hapus Berhasil')
    return redirect ('cek')

#fungsi karyawan
def karyawan(request):
    if request.POST:
        models.karyawan.objects.create(
            nama = request.POST['nama'],
            tanggal_lahir = request.POST['tgl'],
            jabatan = request.POST['jabatan'],
            alamat = request.POST['alamat'],           
            no_hp = request.POST['hp'],
            email = request.POST['mail'],          
            jenis_kelamin = request.POST['jenis_kelamin'],
        )
        messages.success(request, f'Tambah Berhasil')
    data = models.karyawan.objects.all()
    return render(request,'biodata.html',{
        'data': data,
    })
