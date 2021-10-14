from django.urls import path
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    ##path('accueilAdmin', views.formAjoutProInt, name=''),
    path('vetements', views.vetement, name='vetements'),
    path('produitInterieur', views.produitInterieur, name='produitInterieur'),
    path('cosmetique', views.cosmetique, name='cosmetique'),
    path('detailsVet/<int:id>', views.detailsVet, name='detailsVet'),
    path('detailsCos/<int:id>', views.detailsCos, name='detailsCos'),
    path('detailsProInt/<int:id>', views.detailsProInt, name='detailsProInt'),
    path('atelier', views.atelier, name='atelier'),
    path('detailsAtelier/<int:id>', views.detailsAtelier, name='detailsAtelier'),
    path('commande', views.commande, name='commande'),
    path('detailsCommande/<int:id>', views.detailsCommande, name='detailsCommande'),
    path('quiSommesNous',views.quiSommesNous,name='quiSommesNous'),

    path('searchProduit', views.searchProduit, name='searchProduit'),

]