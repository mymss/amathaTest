from django.urls import path
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('accueilAdmin', views.accueilAdmin, name='accueilAdmin'),
    ##path('accueilAdmin', views.formAjoutProInt, name=''),
    path('vetements', views.vetement, name='vetements'),
    path('produitInterieur', views.produitInterieur, name='produitInterieur'),
    path('cosmetique', views.cosmetique, name='cosmetique'),
    path('detailsVet/<int:id>', views.detailsVet, name='detailsVet'),
    path('detailsCos/<int:id>', views.detailsCos, name='detailsCos'),
    path('detailsProInt/<int:id>', views.detailsProInt, name='detailsProInt'),
    path('atelier', views.atelier, name='atelier'),
    path('detailsAtelier/<int:id>', views.detailsAtelier, name='detailsAtelier'),

    path('gestionStock', views.gestionStock, name='gestionStock'),
    path('gestionProduit', views.gestionProduit, name='gestionProduit'),
    path('gestionAtelier', views.gestionAtelier, name='gestionAtelier'),
    path('gestionClient', views.gestionClient, name='gestionClient'),

    path('insertionVetement', views.insertionVetement, name='insertionVetement'),
    path('insertionProInt', views.insertionProInt, name='insertionProInt'),
    path('insertionProCos', views.insertionProCos, name='insertionProCos'),
    path('insertionAtelier', views.insertionAtelier, name='insertionAtelier'),
    path('insertionPhoto', views.insertionPhoto, name='insertionPhoto'),

    path('updateVet/<int:id>', views.updateVet, name='updateVet'),
    path('updateProInt/<int:id>', views.updateProInt, name='updateProInt'),
    path('updateProCos/<int:id>', views.updateProCos, name='updateProCos'),

    path('updateStockVet/<int:id>', views.updateStockVet, name='updateStockVet'),
    path('updateStockProInt/<int:id>', views.updateStockProInt, name='updateStockProInt'),
    path('updateStockProCos/<int:id>', views.updateStockProCos, name='updateStockProCos'),
    path('updateAtelier/<int:id>', views.updateAtelier, name='updateAtelier'),

    path('adminVetDetails/<int:id>', views.adminVetDetails, name='adminVetDetails'),
    path('adminProIntDetails/<int:id>', views.adminProIntDetails, name='adminProIntDetails'),
    path('adminProCosDetails/<int:id>', views.adminProCosDetails, name='adminProCosDetails'),
    path('adminAtelierDetails/<int:id>', views.adminAtelierDetails, name='adminAtelierDetails'),







]