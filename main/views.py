from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http.response import Http404


def index(request):
    return render(request,'index.html')

<<<<<<< HEAD
def register(request):
    return render(request,'register.html')
=======
def index(request):
    return render(request, 'home.html')
# def profil(request):
#     return render(request, 'profil.html')
# def beranda(request):
#     return render(request, 'beranda.html')
>>>>>>> 6994170d9d9747d16fe317ddcc1629ebadab35ce
