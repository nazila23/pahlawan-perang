from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('order/', views.order, name='order'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tambah/', views.tambah, name='tambah'),
    path('usersprof/', views.usersprof, name='usersprof'),
    path('daftarbiblografi/daftaranggota/', views.daftaranggota, name='daftaranggota'),
    path('biblografi/', views.biblografi, name='biblografi'),
    path('daftarbiblografi/', views.daftarbiblografi, name='daftarbiblografi'),
    path('daftarexsemplar/', views.daftarexsemplar, name='daftarexsemplar'),
    path('dataexsemplar/', views.dataexsemplar, name='dataexsemplar'),
    
    
]