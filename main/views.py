from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http.response import Http404


def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')

