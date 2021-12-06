from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http.response import Http404
from django.db.models.base import Model
# Create your views here.


def detail1(request):
    return render(request,'detail1.html')
def detail(request):
    return render(request,'detail.html')
