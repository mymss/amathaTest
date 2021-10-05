from django.urls import path
from . import views


app_name = 'administration'


urlpatterns = [
    path('accueilAdmin/', views.accueilAdmin, name='accueilAdmin'),
    path('gestionStock/', views.gestionStock, name='gestionStock'),
    path('gestionProduit/', views.gestionProduit, name='gestionProduit'),
    path('gestionAtelier/', views.gestionAtelier, name='gestionAtelier'),
    path('gestionClient/', views.gestionClient, name='gestionClient'),
    path('gestionCommande/', views.gestionClient, name='gestionCommande'),

    path('adminVetDetails/<int:id>', views.adminVetDetails, name='adminVetDetails'),
    path('adminProIntDetails/<int:id>', views.adminProIntDetails, name='adminProIntDetails'),
    path('adminProCosDetails/<int:id>', views.adminProCosDetails, name='adminProCosDetails'),
    path('adminAtelierDetails/<int:id>', views.adminAtelierDetails, name='adminAtelierDetails'),
    path('adminClientDetails/<int:id>', views.adminClientDetails, name='adminClientDetails'),

    path('insertionVetement/', views.insertionVetement, name='insertionVetement'),
    path('insertionProInt/', views.insertionProInt, name='insertionProInt'),
    path('insertionProCos/', views.insertionProCos, name='insertionProCos'),
    path('insertionAtelier/', views.insertionAtelier, name='insertionAtelier'),

    path('updateVet/<int:id>', views.updateVet, name='updateVet'),
    path('updateProInt/<int:id>', views.updateProInt, name='updateProInt'),
    path('updateProCos/<int:id>', views.updateProCos, name='updateProCos'),

    path('updateStockVet/<int:id>', views.updateStockVet, name='updateStockVet'),
    path('updateStockProInt/<int:id>', views.updateStockProInt, name='updateStockProInt'),
    path('updateStockProCos/<int:id>', views.updateStockProCos, name='updateStockProCos'),
    path('updateAtelier/<int:id>', views.updateAtelier, name='updateAtelier'),

]