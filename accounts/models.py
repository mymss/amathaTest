# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=500, null=True, blank=True)
    codePostal = models.CharField(max_length=4, null=True, blank=True)
    localite = models.CharField(max_length=500, null=True, blank=True)
    dateNaissance = models.DateField(null=True, blank=True)
    numerosMobile = models.CharField(max_length=12, null=True, blank=True)
    clientActif = models.BooleanField(default=True)

    def __str__(self):
        if self.nom is None and self.prenom is None:
            return str(self.user.email)
        else:
            return self.nom + " " + self.prenom

    # def ddnMin(self):
    #     if self.dateNaissance > datetime.date.today():
    #         return messages.warning(request, 'La date de naissance est erronées.')


@receiver(pre_save, sender=User)
def check_email(sender, instance, **kwargs):
    email = instance.email
    if sender.objects.filter(email=email).exclude(username=instance.username).exists():
        raise ValidationError('Email existant. Revenez en arrière.')