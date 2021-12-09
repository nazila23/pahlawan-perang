from django.urls import path
from . import views

urlpatterns = [
    path('biblografi/', views.biblografi, name='biblografi'),
    path('<id>/delete/', views.delete_anggota),
    path('anggota/', views.anggota, name='anggota'),
    path('exemplar/', views.exemplar, name='exemplar'),
    path('biodata/', views.biodata, name='biodata'),
    path('sirkulasi/', views.sirkulasi, name='sirkulasi'),
    path('sirkulasi/transaksi/', views.transaksi, name='transaksi'),
]