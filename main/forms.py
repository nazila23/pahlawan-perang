# from django import forms
# from django.forms import widgets
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length=30, required=True)
#     password = forms.EmailField(max_length=254, required=True)
        
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', )
#         labels = {
#             'username': _('Username'),
#             'email': _('Email'),
#             'password1': _('Password1'),
#             'password2': _('Password2')
#         }

#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['email'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['class'] = 'form-control'

# from django import forms 
# from .models import Image 
#     class ImageForm(forms.ModelForm): 
#     class Meta: 
#     model=Image 
#     fields=("caption","image") 

