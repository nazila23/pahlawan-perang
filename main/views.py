from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http.response import Http404
from main import forms
from.import models, forms
from django.db.models.base import Model
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main2 import models as main_mod
# from django.contrib.auth.models import user

# sigin

def index(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if user is not None:
                login(request, user)
            return redirect('/')
    else:

        form = SignUpForm()
    return render(request,'index.html', {
        'form': form,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)    
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {
        'form':form,
    })


def order(request):
    return render(request,'order.html')
def dashboard(request):
    return render(request,'dashboard.html')
def tambah(request):
    return render(request,'tambah.html')
def usersprof(request):
    if request.POST:
        main_mod.anggota.objects.filter(id=id).update(
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
        return redirect('usersprof')
    user = main_mod.anggota.objects.all()
    print(user)
    return render(request,'usersprof.html', {
        'data': user,
    })
def usulan(request):
    return render(request,'usulan.html')
def upload(request):
    return render(request,'upload-karya.html')
def order(request):
    return render(request,'order-buku.html')
def bebas(request):
    return render(request,'bebas-pustaka.html')
def history(request):
    return render(request,'history-peminjaman.html')
def katalog(request):
    return render(request,'katalog.html')
def home(request):
    return render(request,'home.html')
def detail1(request):
    return render(request,'detail1.html')
def detail(request):
    return render(request,'detail.html')
