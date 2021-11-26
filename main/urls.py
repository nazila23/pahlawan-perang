from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('order/', views.order, name='order'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('usersprof/', views.usersprof, name='usersprof'),
<<<<<<< HEAD
    path('daftarbiblografi/daftaranggota/', views.daftaranggota, name='daftaranggota'),
    path('biblografi/', views.biblografi, name='biblografi'),
    path('daftarbiblografi/', views.daftarbiblografi, name='daftarbiblografi'),
    path('daftarexsemplar/', views.daftarexsemplar, name='daftarexsemplar'),
    path('dataexsemplar/', views.dataexsemplar, name='dataexsemplar'),
    
    
=======
    path('usulan/', views.usulan, name='usulan'),
    path('upload/', views.upload, name='upload-karya'),
    path('order/', views.order, name='order-buku'),
     path('bebas/', views.bebas, name='bebas-pustaka'),
>>>>>>> 55dd98ff8531180856fa4fc1c82cff567390fceb
]