from datetime import date
import random
from random import randint

import stripe
from django.shortcuts import render
from django.views.generic import TemplateView

from amatha import settings
from cart.models import PanierItem
from shop.models import LigneAtelierCommande, LigneProduitCommande, Commande

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductLandingPageView(TemplateView):
    template_name = "paiement/pages/landing.html"

    def get_context_data(self, **kwargs):
        panier = PanierItem.objects.filter(user=self.request.user)
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)

        prix_total = 0
        for item in panier:
            prix_total += item.price

        prix_total = prix_total * 100

        context.update({
            "prix_total": prix_total,
            "panier": panier,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        })
        return context


def charge(request):
    panier = PanierItem.objects.filter(user=request.user)
    prix_total = 0
    listeArticle = []

    for item in panier:
        if item.product:
            newStock = item.product.stockDisponible - item.quantity
            item.product.stockDisponible = newStock
            item.product.save()
        else:
            newPlaces = item.atelier.nbrPersonneMax - item.quantity
            item.atelier.nbrPersonneMax = newPlaces
            item.atelier.save()

    for item in panier:
        prix_total += item.price
    prix_total = prix_total * 100

    for element in panier:
        clientId = request.user.client
        comTotal = prix_total / 100
        statut = 'En attente'
        produit = element.product
        atelier = element.atelier
        listeArticle.append(element)
        quantite = element.quantity
        comNumero = random.randint(1, 1000)
        comDate = date.today()

    commande = Commande.objects.create(
        clientId=clientId,
        comNumero=comNumero,
        comTotal=comTotal,
        statut=statut,
        comDate=comDate,
    )

    for art in listeArticle:
        if art.product is not None:
            ligneProCom = LigneProduitCommande.objects.create(
                produit=art.product,
                commande=commande,
                quantite=art.quantity,
            )
        if art.atelier is not None:
            ligneAteCom = LigneAtelierCommande.objects.create(
                atelier=art.atelier,
                commande=commande,
                nbrPersonne=art.quantity
            )

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=prix_total,
            currency='chf',
            description='amatha facture',
            source=request.POST['stripeToken']
        )

        return render(request, 'paiement/pages/charge.html')


def handler404(request,exception):
    return render(request, 'paiement/pages/404.html', status=404)


def handler500(request):
    return render(request, 'paiement/pages/500.html', status=500)
