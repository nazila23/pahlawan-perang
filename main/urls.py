from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('register/', views.register, name='register'),
=======
    # path('profil/', views.profil, name='profil'),
    # path('beranda/', views.beranda, name='beranda'),
>>>>>>> 6994170d9d9747d16fe317ddcc1629ebadab35ce
]