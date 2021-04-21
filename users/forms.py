from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name','username', 'email')
        
        
        
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label=('First name: '),max_length=(100))
    last_name = forms.CharField(label=('Last name: '),max_length=(100))
    username = forms.CharField(label=('Username: '),max_length=(100))
    email = forms.EmailField(label=('Email Address: '))
    
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
    
class ProfileUpdateForm(forms.ModelForm):
    img = forms.ImageField(label=('Profile Picture: '),required=False, widget=forms.FileInput)
    cover_img = forms.ImageField(label=('Cover Photo: '),required=False, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['img','cover_img']