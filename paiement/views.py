import stripe
from django.shortcuts import render
from django.views.generic import TemplateView

from amatha import settings
from cart.models import PanierItem

stripe.api_key = settings.STRIPE_SECRET_KEY

class ProductLandingPageView(TemplateView):
    template_name = "paiement/pages/landing.html"


    def get_context_data(self, **kwargs):
        panier = PanierItem.objects.filter(user = self.request.user)
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)

        prix_total = 0
        for item in panier:
            prix_total += item.price

        prix_total = prix_total * 100

        context.update({
            "prix_total" : prix_total,
            "panier" : panier,
            "STRIPE_PUBLIC_KEY" : settings.STRIPE_PUBLIC_KEY,
        })
        return context

def charge(request):
    panier = PanierItem.objects.filter(user=request.user)
    prix_total = 0
    for item in panier:
        prix_total += item.price

    prix_total = prix_total * 100

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=prix_total,
            currency='chf',
            description='amatha facture',
            source=request.POST['stripeToken']
        )
        return render(request, 'paiement/pages/charge.html')