from django.db import models
from accounts.models import User
from shop.models import Produit, Prix
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Panier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)

class PanierItem(models.Model):
    cart = models.ForeignKey(Panier, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username) + " " + str(self.product.nom)

@receiver(pre_save, sender=PanierItem)
def correct_price(sender, **kwargs):
    cart_item = kwargs['instance']
    product = Produit.objects.get(id = cart_item.product.id)
    price_of_product = Prix.objects.get(produit = product.id)
    cart_item.price = cart_item.quantity * float(price_of_product.montant)


    total_cart_items = PanierItem.objects.filter(user = cart_item.user)
    cart = Panier.objects.get(id = cart_item.cart.id)

    total = 0
    for item in total_cart_items:
        total += item.price

    total += cart_item.price

    print(total_cart_items)
    cart.total_price = total
    cart.save()