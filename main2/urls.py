from django.urls import path
from . import views

urlpatterns = [
    path('', views.biblografi, name='biblografi'),
    path('anggota/', views.anggota, name='anggota'),
    path('anggota/<id>/delete_anggota', views.delete_anggota),
    path('exemplar/', views.exemplar, name='exemplar'),
    path('biodata/', views.biodata, name='biodata'),
    path('sirkulasi/', views.sirkulasi, name='sirkulasi'),
    path('sidebarpustaka/', views.sidebarpustaka, name='sidebarpustaka'),
    path('anggota/<id>/edit_anggota', views.edit_anggota,name='edit_anggota'),
    path('anggota/<id>/detail_anggota', views.detail_anggota,name='detail_anggota'),
    path('transaksi/', views.transaksi, name='transaksi'),
    path('login/', views.login, name='login'),
    
]