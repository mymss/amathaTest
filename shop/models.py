from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    stockMin = models.IntegerField()
    stockMax = models.IntegerField()
    stockDisponible = models.IntegerField()
    poid = models.DecimalField(max_digits=4, decimal_places=2)
    favoris = models.ManyToManyField(User, related_name='favoris', blank=True)

    def get_absolute_url(self):
        return reverse('index',args=[str(self.id)])

    def __str__(self):
        return self.nom


class Vetement(Produit):
    sexe = models.CharField(max_length=20)
    typeTissu = models.CharField(max_length=50)
    couleur = models.CharField(max_length=20)
    taille = models.CharField(max_length=20)

    def __str__(self):
        return self.nom + " " + self.sexe + " " + self.taille + " " + self.couleur


class ProduitInterieur(Produit):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.nom + " " + self.type


class Cosmetique(Produit):
    ingredient = models.CharField(max_length=100)
    gamme = models.CharField(max_length=50)
    categorie = models.CharField(max_length=50)

    def __str__(self):
        return self.nom + " " + self.gamme + " " + self.categorie


class Prix(models.Model):
    montant = models.IntegerField()
    reduction = models.IntegerField()
    date = models.DateField(auto_now_add=False)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.montant)


class Atelier(models.Model):
    titre = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    nbrPersonneMax = models.IntegerField()
    dateDebut = models.DateField(auto_now_add=False)
    heureDebut = models.TimeField(auto_now_add=False)
    heureFin = models.TimeField(auto_now_add=False)
    adresse = models.CharField(max_length=150)
    prix = models.IntegerField()

    def __str__(self):
        return self.titre


class Photo(models.Model):
    url = models.CharField(max_length=30)
    nomFichier = models.CharField(max_length=30)
    produitId = models.ForeignKey(Produit, on_delete=models.CASCADE, blank=True,null=True)
    # atelierId = models.ForeignKey(Atelier, on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.nomFichier

