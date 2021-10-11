from django.conf.urls import url
from django.urls import path
from .views import CreateCheckoutSessionView, ProductLandingPageView

app_name = 'paiement'

urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
    path('', ProductLandingPageView.as_view(), name="landing-page")
]
