from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Client


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   }))


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    dateNaissance = forms.DateField(label='dateNaissance', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))

    class Meta:
        model = Client
        fields = ('nom', 'prenom','mail', 'adresse', 'codePostal','localite','dateNaissance', 'numerosMobile')


class InfosUpdateForm(forms.ModelForm):
    dateNaissance = forms.DateField(label='dateNaissance', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    class Meta:
        model = Client
        fields = ('nom', 'prenom','mail', 'adresse', 'codePostal','localite','dateNaissance', 'numerosMobile')