from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
 
 
class RegistrForm(UserCreationForm):
  email = forms.EmailField(max_length=254)
  

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', )

class UserAuthentication(AuthenticationForm):
  
  class Meta:
    model = User
    fields = ['username', 'password']

  
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'last_name', 'first_name', 'email']

class ProfileImage(forms.ModelForm):

	def __init__(self, *args, **kwards):
		super(ProfileImage, self).__init__(*args, **kwards)
		self.fields['img'].label = 'Изображение профиля'
		self.fields['phone'].label = 'Номер телефона'
		self.fields['country'].label = 'Страна'
		self.fields['city'].label = 'Город'
		self.fields['address'].label = 'Адрес'

	class Meta:
		model = Profile
		fields = ['img', 'phone', 'country', 'city', 'address']
