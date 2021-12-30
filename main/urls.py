from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('register/', views.register, name='register'),
    path('order/', views.order, name='order'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('usersprof/', views.usersprof, name='usersprof'),
    path('usulan/', views.usulan, name='usulan'),
    path('upload/', views.upload, name='upload-karya'),
    path('order/', views.order, name='order-buku'),
    path('bebas/', views.bebas, name='bebas-pustaka'),
    path('history/', views.history, name='history-peminjaman'),
    path('katalog/', views.katalog, name='katalog'),
    path('home/', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('detail1/', views.detail1, name='detail1'),
    path('sidebarpustaka/', views.sidebarpustaka, name='sidebarpustaka'),
    path('usulan/<id>/edit_usulan', views.edit_usulan, name='edit_usulan'),
    path('usulan/<id>/delete_usulan', views.delete_usulan, name='delet_usulan'),
    path('usulan/<id>/detail_usulan', views.detail_usulan, name='detail_usulan'),

    
]