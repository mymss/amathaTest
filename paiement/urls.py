from django.urls import path
from .views import ProductLandingPageView

app_name = 'paiement'

urlpatterns = [
    path('', ProductLandingPageView.as_view(), name="landing-page")
]
