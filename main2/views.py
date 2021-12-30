from django.contrib import messages
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.http.response import Http404
from django.db.models.base import Model
from.import models
from django.db.models import Q
# Create your views here. 

#Fungsi Biblografi
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
            info_detail_spesifikasi = request.POST['info_detail_spesifikasi'],
            tipe_isi = request.POST['tipe_isi'],
            tipe_media = request.POST['tipe_media'],
            isbn = request.POST['isbn'],
            penerbit = request.POST['penerbit'],
            tahun_terbit = request.POST['tahun_terbit'],
            tempat_terbit = request.POST['tempat_terbit'],
            diskripsi_fisik = request.POST['diskripsi_fisik'],
            klasifikasi = request.POST['klasifikasi'],
            no_panggil = request.POST['no_panggil'],
            bahasa = request.POST['bahasa'],
            cover = request.POST['cover'],
            opac = request.POST['opac'],
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
            tanggal_registrasi = request.POST['tr'],
            berlaku_hingga = request.POST['bg'],
            tipe_anggota = request.POST['tk'],
            pekerjaan = request.POST['pekerjaan'],
            alamat = request.POST['almt'],
            negara = request.POST['negara'],
            no_hp = request.POST['hp'],
            email = request.POST['email'],
            instansi = request.POST['ins'],
            jenis_kelamin = request.POST['jenis_kelamin'],
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
            negara = request.POST ['negara'],
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
    if request.POST:
        beranda = request.POST['gridRadios']
        print(beranda)
        models.exemplar.objects.create(
            judul = request.POST['Judul'],
            pengarang = request.POST['Pengarang'],
            kode_exemplar = request.POST['k_exemplar'],
            no_panggil = request.POST['no_panggil'],
            kode_inventaris = request.POST['k_inventaris'],
            lokasi = request.POST['lokasi'],
            # exemplar = request.POST ['exemplar'],
            # kode_pemesanan = request.POST ['k_pemesanan'],
            tgl_pesan = request.POST['t_pemesanan'],
            tgl_terima = request.POST['t_penerima'],
            promosi = request.POST['gridRadios'],
        )
    data=models.exemplar.objects.all()
    return render(request,'exemplar.html',{
        'data': data,
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
    if request.POST:
        bakul=models.buku.objects.filter(pk=request.POST['buku']).first()
        print(bakul)
        models.pinjam.objects.create(
        no_pang=bakul,
        tgl_pinjam=request.POST['tp'],
        tgl_kembali=request.POST['tk'],
        judul=request.POST['judul'],
    )
        # models.pinjam.objects.create(
        #     no_pang=bakul,
        #     tgl_pinjam=request.POST['tp'],
        #     tgl_kembali=request.POST['tk'],
        #     judul=request.POST['judul']
        # )
        # return redirect(request,'peminjaman.html')
    data_pinjaman=models.pinjam.objects.filter(no_pang=id)
    data = models.anggota.objects.filter(id=id).first()
    buku= models.buku.objects.all()
    print(buku)
    return render(request,'peminjaman.html',{
        'data' :data,
        'data_pinjaman': data_pinjaman,
        'buku': buku,
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