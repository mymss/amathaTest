import stripe
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

        context.update({
            "prix_total" : prix_total,
            "panier" : panier,
            "STRIPE_PUBLIC_KEY" : settings.STRIPE_PUBLIC_KEY,
        })
        return context