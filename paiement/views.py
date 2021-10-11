import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views import View

stripe.api_key = settings.STRIPE_SECRET_KEY

class ProductLandingPageView(TemplateView):
    template_name = "paiement/pages/landing.html"

    def get_context_data(self, **kwargs):
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLIC_KEY" : settings.STRIPE_PUBLIC_KEY
        })
        return context

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # TODO: replace this with the `price` of the product you want to sell
                    # 'price': '{FAUT CHERCHER LE PRIX DU PANIER DU BOUG}',
                    'quantity': 1,
                },
            ],
            payment_method_types=[
                'card',
            ],
            mode='payment',
            # url qui nous mènes a la page du paiment reussi
            success_url=YOUR_DOMAIN + '/success/',
            # url qui nous mene a la page d'annulation de paiement
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
