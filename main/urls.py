from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('order/', views.order, name='order'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('usersprof/', views.usersprof, name='usersprof'),
    path('usulan/', views.usulan, name='usulan'),
    path('upload/', views.upload, name='upload-karya'),
    path('order/', views.order, name='order-buku'),
    path('bebas/', views.bebas, name='bebas-pustaka'),
    path('daftaranggota/', views.daftaranggota, name='daftaranggota'),
    path('biblografi', views.biblografi, name='biblografi'),
    path('daftarbiblografi/',views.daftarbiblografi, name='daftarbiblografi'),
    path('daftarexemplar/', views.daftarexemplar, name='daftarexemplar'),
    path('dataexemplar/', views.dataexemplar, name='dataexemplar'),
    path('detail/', views.detail, name='detail'),
    path('detail1/', views.detail1, name='detail1'),
    path('tambahanggota/', views.tambahanggota, name='tambahanggota'),
]