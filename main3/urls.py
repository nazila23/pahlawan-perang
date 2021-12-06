from django.urls import path
from . import views

urlpatterns = [
    path('detail/', views.detail, name='detail'),
    path('detail1/', views.detail1, name='detail1'),
]