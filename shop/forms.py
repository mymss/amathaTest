from django import forms

from accounts.models import Client
from .models import Produit, Vetement, ProduitInterieur, Cosmetique, Atelier, Prix


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
            'poid': 'Poid',
            'produitActif': 'Produit actif',
            'nomFichier': 'Nom fichier',
            'sexe': 'Sexe',
            'typeTissu': 'Type tissu',
            'couleur': 'Couleur',
            'taille': 'Taille'
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
            'poid': 'Poid',
            'produitActif': 'Produit actif',
            'nomFichier': 'Nom fichier',
            'type': 'Type'
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
            'poid': 'Poid',
            'produitActif': 'Produit actif',
            'nomFichier': 'Nom fichier',
            'ingredient': 'Ingrédients',
            'gamme': 'Gamme',
            'categorie': 'Catégorie'
        }


### Form Insertion Atelier
class PosteInsertAtelier(forms.ModelForm):
    class Meta:
        model = Atelier
        fields = (
            'titre', 'description', 'nbrPersonneMax', 'dateDebut', 'heureDebut', 'heureFin', 'adresse', 'prix',
            'AtelierActif', 'nomFichier')
        labels = {
            'titre' : 'Titre',
            'description': 'Description',
            'nbrPersonneMax': 'Nombre de personne',
            'dateDebut': 'Date début',
            'heureDebut': 'Heure début',
            'heureFin': 'Heure fin',
            'adresse': 'Adresse',
            'prix': 'Prix',
            'AtelierActif': 'Atelier actif',
            'nomFichier': 'Nom fichier',
        }


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


### Form Update Stock Produits Intérieurs
class PosteUpdateStockProInt(forms.ModelForm):
    class Meta:
        model = ProduitInterieur
        fields = (
            'stockDisponible',)
        labels = {
            'stockDisponible': 'Stock disponible',
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


### Form Désactiver un client
class PosteDesativerClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'clientActif',)
        labels = {
            'clientActif': 'Client actif'
        }
