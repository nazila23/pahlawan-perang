from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
<<<<<<< HEAD
    path('order/', views.order, name='order'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tambah/', views.tambah, name='tambah'),
]
=======
    path('usersprof/', views.usersprof, name='usersprof'),
]
>>>>>>> 08eea0039e7f69205b1c23f4579431d38e3b1503
