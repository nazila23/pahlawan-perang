from django.forms import ModelForm
from django.forms import ClearableFileInput
from crispy_forms.helper import FormHelper
from . import models



# class BukuForm(ModelForm):
#     class Meta :
#         model = models.Buku
#         fields = ['upload_img']
#         widgets = {
#             'upload_img': ClearableFileInput(attrs={'multiple': True}),
#         }
# class AnggotaForm(ModelForm):
#     class Meta :
#         model =  models.Anggota
#         exclude =  []