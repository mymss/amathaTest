from django.conf.urls import url
from django.urls import path
from .views import panier, add_to_cart_cos, add_to_cart_proInt, add_to_cart_vet, delete_from_cart, update_quantity_more, \
    update_quantity_less, add_to_cart_atelier, add_to_cart_produit_search

app_name = 'cart'

urlpatterns = [
    path('panier/', panier, name='panier'),
    path('panier_add_cos/<int:id>', add_to_cart_cos, name="add_to_cart_cos"),
    path('panier_add_proInt/<int:id>', add_to_cart_proInt, name="add_to_cart_proInt"),
    path('panier_add_vet/<int:id>', add_to_cart_vet, name="add_to_cart_vet"),
    path('panier_add_atelier/<int:id>', add_to_cart_atelier, name="add_to_cart_atelier"),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_from_cart'),
    url(r'^item/update_more/(?P<item_id>[-\w]+)/$', update_quantity_more, name='update_quantity_more'),
    url(r'^item/update_less/(?P<item_id>[-\w]+)/$', update_quantity_less, name='update_quantity_less'),

    ######## Bar de Recherche ###########
    path('add_to_cart_produit_search/<int:id>', add_to_cart_produit_search, name="add_to_cart_produit_search"),
]