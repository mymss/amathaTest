from django import forms
from .models import Produit, Vetement, ProduitInterieur, Cosmetique, Atelier


### Form Insertion Vetêment
class PosteInsertVet(forms.ModelForm):
    class Meta:
        model = Vetement
        fields = (
            'nom', 'description', 'stockMin', 'stockMax', 'stockDisponible', 'poid', 'produitActif', 'sexe', 'typeTissu', 'couleur',
            'taille')


### Form Insertion Produit Intérieur
class PosteInsertProInt(forms.ModelForm):
    class Meta:
        model = ProduitInterieur
        fields = (
            'nom', 'description', 'stockMin', 'stockMax', 'stockDisponible', 'poid', 'produitActif', 'type')


### Form Insertion Produit Cosmétique
class PosteInsertProCos(forms.ModelForm):
    class Meta:
        model = Cosmetique
        fields = (
            'nom', 'description', 'stockMin', 'stockMax', 'stockDisponible', 'poid', 'produitActif', 'ingredient', 'gamme', 'categorie')


### Form Insertion Atelier
class PosteInsertAtelier(forms.ModelForm):
    class Meta:
        model = Atelier
        fields = (
            'titre', 'description', 'nbrPersonneMax', 'dateDebut', 'heureDebut', 'heureFin', 'adresse', 'prix')


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


### Form Update Stock Produits Intérieurs
class PosteUpdateStockProInt(forms.ModelForm):
    class Meta:
        model = ProduitInterieur
        fields = (
            'stockDisponible',)


### Form Update Stock Vetêment
class PosteUpdateStockProCos(forms.ModelForm):
    class Meta:
        model = Cosmetique
        fields = (
            'stockDisponible',)
