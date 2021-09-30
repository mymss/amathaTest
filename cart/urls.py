from django.conf.urls import url
from django.urls import path
from .views import panier, add_to_cart_cos, add_to_cart_proInt, add_to_cart_vet, delete_from_cart

app_name = 'cart'

urlpatterns = [
    path('panier/', panier, name='panier'),
    path('panier_add_cos/<int:id>', add_to_cart_cos, name="add_to_cart_cos"),
    path('panier_add_proInt/<int:id>', add_to_cart_proInt, name="add_to_cart_proInt"),
    path('panier_add_vet/<int:id>', add_to_cart_vet, name="add_to_cart_vet"),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_from_cart'),
]