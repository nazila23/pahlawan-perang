from django.core.checks import messages
from django.shortcuts import render
from django.http.response import Http404
# from django.shortcuts import redirect, render
# from.import models



def index(request):
    return render(request, 'home.html')
# def profil(request):
#     return render(request, 'profil.html')
# def beranda(request):
#     return render(request, 'beranda.html')
