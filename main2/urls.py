from django.urls import path
from . import views

urlpatterns = [
    path('', views.biblografi, name='biblografi'),
    path('<id>/edit_biblografi', views.edit_biblografi,name='edit_biblografi'),
    path('<id>/delete_biblografi', views.delete_biblografi),
    path('<id>/detail_biblografi', views.detail_biblografi,name='detail_biblografi'),
    path('anggota/', views.anggota, name='anggota'),
    path('anggota/<id>/edit_anggota', views.edit_anggota,name='edit_anggota'),
    path('anggota/<id>/detail_anggota', views.detail_anggota,name='detail_anggota'),
    path('anggota/<id>/delete_anggota', views.delete_anggota),
    path('exemplar/', views.exemplar, name='exemplar'),
    path('biodata/', views.biodata, name='biodata'),
    path('sirkulasi/', views.sirkulasi, name='sirkulasi'),
    path('sidebarpustaka/', views.sidebarpustaka, name='sidebarpustaka'),
    path('sirkulasi/transaksi/', views.transaksi, name='transaksi'),

]