from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Client



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control',
                                                                               }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
                                                                                   }))

class UserForm(UserCreationForm):
    username = forms.CharField(label ='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control',
                                                                               }))
    email = forms.CharField(label ='Email',widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
                                                                               }))
    password1 = forms.CharField(label ='Password',widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
                                                                                   }))
    password2 = forms.CharField(label ='Password confirmation',widget=forms.PasswordInput(attrs={
        'placeholder': 'Password confirmation',
        'class': 'form-control',
                                                                                   }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    dateNaissance = forms.DateField(label='dateNaissance', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))

    class Meta:
        model = Client
        fields = ('dateNaissance',)


class InfosUpdateForm(forms.ModelForm):
    nom = forms.CharField(label='Nom', widget=forms.TextInput(attrs={
        'placeholder': 'Nom',
        'class': 'form-control',
    }))
    prenom = forms.CharField(label='Prénom', widget=forms.TextInput(attrs={
        'placeholder': 'Prénom',
        'class': 'form-control',
    }))
    adresse = forms.CharField(label='Adresse', widget=forms.TextInput(attrs={
        'placeholder': 'Adresse',
        'class': 'form-control',
    }))
    codePostal = forms.CharField(label='Code postal', widget=forms.TextInput(attrs={
        'placeholder': 'Code postal',
        'class': 'form-control',
    }))
    localite = forms.CharField(label='Localité', widget=forms.TextInput(attrs={
        'placeholder': 'Localité',
        'class': 'form-control',
    }))
    dateNaissance = forms.DateField(label='dateNaissance', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    numerosMobile = forms.CharField(label='Numéro mobile', widget=forms.TextInput(attrs={
        'placeholder': 'Numéro mobile',
        'class': 'form-control',
    }))
    class Meta:
        model = Client
        fields = ('nom', 'prenom', 'adresse', 'codePostal','localite','dateNaissance', 'numerosMobile')

class EmailUpdateForm(forms.ModelForm):
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
    }))
    email2 = forms.CharField(label='Email confirmation', widget=forms.TextInput(attrs={
        'placeholder': 'Email confirmation',
        'class': 'form-control',
    }))
    class Meta:
        model = User
        fields = ('email',)

class PasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(label='old_password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Ancien mot de passe',
        'class': 'form-control',
    }))
    new_password1 = forms.CharField(label='new_password1', widget=forms.PasswordInput(attrs={
        'placeholder': 'Nouveau mot de passe',
        'class': 'form-control',
    }))
    new_password2 = forms.CharField(label='new_password2', widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmation mot de passe',
        'class': 'form-control',
    }))
    class Meta:
        model = User
        fields = ('password',)