from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.EmailField(max_length=254, null=True, blank=True)
    adresse = models.CharField(max_length=500,null=True, blank=True)
    codePostal = models.CharField(max_length=4, blank=True)
    localite = models.CharField(max_length=500,null=True, blank=True)
    dateNaissance = models.DateField()
    numerosMobile = models.CharField(max_length=12)
    clientActif = models.BooleanField(default=True)

    def __str__(self):
        return self.nom



