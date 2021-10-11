from django.db import models
from accounts.models import User
from shop.models import Produit, Prix, Atelier
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
    atelier = models.ForeignKey(Atelier, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username) + " " + str(self.product.nom) + " " + str(self.quantity)

@receiver(pre_save, sender=PanierItem)
def correct_price(sender, **kwargs):
    cart_item = kwargs['instance']
    productInst = Produit.objects.get(id=cart_item.product.id)
    price_of_product = Prix.objects.get(produit=productInst.id)
    cart_item.price = cart_item.quantity * float(price_of_product.montant)

    cart = Panier.objects.get(id=cart_item.cart.id)
    total_cart_items = PanierItem.objects.filter(cart_id=cart.id)

    total = 0
    for item_prix in total_cart_items.exclude(id=cart_item.id):
        total += item_prix.price
    total += cart_item.price

    cart.total_price = total
    cart.save()
