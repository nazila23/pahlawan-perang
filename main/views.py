from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http.response import Http404
from main import forms
from.import models, forms
from django.db.models.base import Model
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request,'index.html', {
        'form': form,
    })
# def register(request):
#     return render(request,'register.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return redirect('home')
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
def daftarbiblografi(request):
    return render(request,'daftarbiblografi.html')
def daftaranggota(request):
    return render(request,'daftaranggota.html')
def dataexemplar(request):
    return render(request,'daftarexsemplar.html')


