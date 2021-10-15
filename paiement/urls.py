from django.urls import path
from . import views
from .views import ProductLandingPageView

app_name = 'paiement'

urlpatterns = [
    path('', ProductLandingPageView.as_view(), name="landing-page"),
    path('charge/', views.charge, name="charge")
]
