from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http.response import Http404


def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
<<<<<<< HEAD
def order(request):
    return render(request,'order.html')
def dashboard(request):
    return render(request,'dashboard.html')
def tambah(request):
    return render(request,'tambah.html')
=======
def usersprof(request):
    return render(request,'usersprof.html')
>>>>>>> 08eea0039e7f69205b1c23f4579431d38e3b1503

