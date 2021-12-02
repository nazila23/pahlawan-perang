from django.urls import path
from . import views

urlpatterns = [
    path('biblografi/', views.biblografi, name='biblografi'),
    path('daftarbiblografi/', views.daftarbiblografi, name='daftarbiblografi'),
    path('daftaranggota/', views.daftaranggota, name='daftaranggota'),
    path('dataexemplar/', views.dataexemplar, name='dataexemplar'),
]