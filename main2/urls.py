from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.biblografi, name='biblografi'),
    path('<id>/edit_biblografi', views.edit_biblografi,name='edit_biblografi'),
    path('<id>/delete_biblografi', views.delete_biblografi),
    path('<id>/detail_biblografi', views.detail_biblografi,name='detail_biblografi'),
    path('anggota/', views.anggota, name='anggota'),
    path('anggota/<id>/edit_anggota', views.edit_anggota,name='edit_anggota'),
    path('anggota/<id>/detail_anggota', views.detail_anggota,name='detail_anggota'),
    path('anggota/<id>/delete_anggota', views.delete_anggota,name='delete_anggota'),
    path('exemplar/', views.exemplar, name='exemplar'),
    path('exemplar/<id>/edit_exemplar', views.edit_exemplar,name='edit_exemplar'),
    path('exemplar/<id>/detail_exemplar', views.detail_exemplar,name='detail_exemplar'),
    path('exemplar/<id>/delete_exemplar', views.delete_exemplar),
    path('biodata/', views.biodata, name='biodata'),
    path('sirkulasi/', views.sirkulasi, name='sirkulasi'),
    path('sidebarpustaka/', views.sidebarpustaka, name='sidebarpustdeaka'),
    # path('peminjaman/', views.peminjaman,name='peminjaman'),
    path('peminjaman/<id>/', views.peminjaman,name='peminjaman'),
    path('peminjaman/<id>/delete_pinjam/', views.delete_pinjam),
    path('cek/', views.cek, name='cek'),
    path('cek/<id>/delete_cek', views.delete_cek),
    path('karyawan/', views.karyawan, name='karyawan'),      
]
if settings.DEBUG: urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




