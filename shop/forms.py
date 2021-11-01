import datetime
from datetime import date

from django import forms

from accounts.models import Client
from .models import Produit, Vetement, ProduitInterieur, Cosmetique, Atelier, Prix, Commande


### Form Insertion Vetêment
class PosteInsertVet(forms.ModelForm):
    class Meta:
        model = Vetement
        fields = (
            'nom', 'description', 'stockMin', 'stockMax', 'stockDisponible', 'poid', 'produitActif', 'nomFichier',
            'sexe', 'typeTissu', 'couleur', 'taille',)
        labels = {
            'nom': 'Nom',
            'description': 'Description',
            'stockMin': 'Stock minimum',
            'stockMax': 'Stock maximum',
            'stockDisponible': 'Stock disponible',
            'poid': 'Poid en gramme',
            'produitActif': 'Produit actif',
            'nomFichier': 'Nom fichier',
            'sexe': 'Sexe',
            'typeTissu': 'Type tissu',
            'couleur': 'Couleur',
            'taille': 'Taille'
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            # 'description': forms.Textarea(attrs={'row': 3})
            'description': forms.Textarea(attrs={'row': 3, 'class': 'form-control'}),
            'stockMin': forms.TextInput(attrs={'class': 'form-control'}),
            'stockMax': forms.TextInput(attrs={'class': 'form-control'}),
            'stockDisponible': forms.TextInput(attrs={'class': 'form-control'}),

            'poid': forms.TextInput(attrs={'class': 'form-control'}),
            # 'nomFichier': forms.ImageField(attrs={'class': 'form-control'}),
            'sexe': forms.TextInput(attrs={'class': 'form-control'}),
            'typeTissu': forms.TextInput(attrs={'class': 'form-control'}),
            'couleur': forms.TextInput(attrs={'class': 'form-control'}),
            'taille': forms.TextInput(attrs={'class': 'form-control'}),

        }


### Form Insertion Produit Intérieur
class PosteInsertProInt(forms.ModelForm):
    class Meta:
        model = ProduitInterieur
        fields = (
            'nom', 'description', 'stockMin', 'stockMax', 'stockDisponible', 'poid', 'produitActif', 'nomFichier',
            'type')
        labels = {
            'nom': 'Nom',
            'description': 'Description',
            'stockMin': 'Stock minimum',
            'stockMax': 'Stock maximum',
            'stockDisponible': 'Stock disponible',
            'poid': 'Poid en gramme',
            'produitActif': 'Produit actif',
            'nomFichier': 'Nom fichier',
            'type': 'Type'
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            # 'description': forms.Textarea(attrs={'row': 3})
            'description': forms.Textarea(attrs={'row': 3, 'class': 'form-control'}),
            'stockMin': forms.TextInput(attrs={'class': 'form-control'}),
            'stockMax': forms.TextInput(attrs={'class': 'form-control'}),
            'stockDisponible': forms.TextInput(attrs={'class': 'form-control'}),
            'poid': forms.TextInput(attrs={'class': 'form-control'}),
            # 'nomFichier': forms.ImageField(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
        }


### Form Insertion Produit Cosmétique
class PosteInsertProCos(forms.ModelForm):
    class Meta:
        model = Cosmetique
        fields = (
            'nom', 'description', 'stockMin', 'stockMax', 'stockDisponible', 'poid', 'produitActif', 'nomFichier',
            'ingredient', 'gamme', 'categorie')
        labels = {
            'nom': 'Nom',
            'description': 'Description',
            'stockMin': 'Stock minimum',
            'stockMax': 'Stock maximum',
            'stockDisponible': 'Stock disponible',
            'poid': 'Poid en gramme',
            'produitActif': 'Produit actif',
            'nomFichier': 'Nom fichier',
            'ingredient': 'Ingrédients',
            'gamme': 'Gamme',
            'categorie': 'Catégorie'
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'row': 3, 'class': 'form-control'}),
            'stockMin': forms.TextInput(attrs={'class': 'form-control'}),
            'stockMax': forms.TextInput(attrs={'class': 'form-control'}),
            'stockDisponible': forms.TextInput(attrs={'class': 'form-control'}),
            'poid': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredient': forms.TextInput(attrs={'class': 'form-control'}),
            'gamme': forms.TextInput(attrs={'class': 'form-control'}),
            'categorie': forms.TextInput(attrs={'class': 'form-control'}),
        }


### Form Insertion Atelier
class PosteInsertAtelier(forms.ModelForm):
    class Meta:
        model = Atelier
        fields = (
            'titre', 'description', 'nbrPersonneMax', 'dateDebut', 'heureDebut', 'heureFin', 'adresse', 'prix',
            'AtelierActif', 'nomFichier')
        labels = {
            'titre': 'Titre',
            'description': 'Description',
            'nbrPersonneMax': 'Nombre de personne maximum',
            'dateDebut': 'Date début',
            'heureDebut': 'Heure début',
            'heureFin': 'Heure fin',
            'adresse': 'Adresse',
            'prix': 'Prix',
            'AtelierActif': 'Atelier actif',
            'nomFichier': 'Nom fichier',
        }
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'row': 3, 'class': 'form-control'}),
            'nbrPersonneMax': forms.NumberInput(attrs={'class': 'form-control'}),
            'dateDebut': forms.DateInput(attrs={'class': 'form-control'}),
            'heureDebut': forms.TimeInput(attrs={'class': 'form-control'}),
            'heureFin': forms.TimeInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'step': 0.25, 'class': 'form-control'}),
        }

        # def clean_dateDebut(self, *args, **kwargs):
        #     dateAtelier = self.cleaned_data.get("dateDebut")
        #     if dateAtelier > datetime.date.today():
        #         return dateAtelier
        #     else:
        #         raise forms.ValidationError("La date d'un atelier doit être supérieur à la date d'aujourd'hui")

        def __init__(self):
            self.cleaned_data = None

        def clean(self, *args, **kwargs):
            # cleaned_data = super().clean()
            dateAtelier = self.cleaned_data['dateDebut']
            if dateAtelier.get('dateAtelier') > datetime.date.today():
                return dateAtelier
            else:
                raise forms.ValidationError("La date d'un atelier doit être supérieur à la date d'aujourd'hui")


# ###################### TEST INSERTION PHOTO ############################
# ### Form Insertion Photo
# class PosteInsertPhoto(forms.ModelForm):
#     class Meta:
#         model = Photo
#         fields = (
#             'url', 'nomFichier', 'produitId', 'atelierId')
#

### Form Update Stock Vetêment
class PosteUpdateStockVet(forms.ModelForm):
    class Meta:
        model = Vetement
        fields = (
            'stockDisponible',)
        labels = {
            'stockDisponible': 'Stock disponible',
        }
        widgets = {
            'stockDisponible': forms.NumberInput(attrs={'class': 'form-control'}),
        }


### Form Update Stock Produits Intérieurs
class PosteUpdateStockProInt(forms.ModelForm):
    class Meta:
        model = ProduitInterieur
        fields = (
            'stockDisponible',)
        labels = {
            'stockDisponible': 'Stock disponible',
        }
        widgets = {
            'stockDisponible': forms.NumberInput(attrs={'class': 'form-control'}),
        }

### Form Update Stock Vetêment
class PosteUpdateStockProCos(forms.ModelForm):
    class Meta:
        model = Cosmetique
        fields = (
            'stockDisponible',)
        labels = {
            'stockDisponible': 'Stock disponible',
        }
        widgets = {
            'stockDisponible': forms.NumberInput(attrs={'class': 'form-control'}),
        }


### Form Update Prix
class PosteUpdatePrix(forms.ModelForm):
    class Meta:
        model = Prix
        fields = (
            'montant', 'reduction', 'date',)
        labels = {
            'montant': 'Montant',
            'reduction': 'Réduction',
            'date': 'Date',
        }
        widgets = {
            'montant': forms.NumberInput(attrs={'step': 0.25, 'class': 'form-control'}),
            'reduction': forms.NumberInput(attrs={'step': 0.25, 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }


### Form Update Prix
class PosteInsertPrix(forms.ModelForm):
    class Meta:
        model = Prix
        fields = (
            'montant', 'reduction', 'date', 'produit')
        labels = {
            'montant': 'Montant',
            'reduction': 'Réduction',
            'date': 'Date',
            'produit': 'Nom produit'
        }
        widgets = {
            'montant': forms.NumberInput(attrs={'step': 0.25, 'class': 'form-control'}),
            'reduction': forms.NumberInput(attrs={'step': 0.25, 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'produit': forms.Select(attrs={'class': 'form-control'}),
            # 'produit': Produit.objects.last().id
        }


### Form Désactiver un client
class PosteDesativerClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'clientActif',)
        labels = {
            'clientActif': 'Client actif'
        }

### Form Update Stock Vetêment
class PosteUpdateStatutCommande(forms.ModelForm):
    class Meta:
        model = Commande
        fields = (
            'statut',)
        labels = {
            'statut': 'Statut',
        }
        widgets = {
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }

