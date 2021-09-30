from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from cart.models import PanierItem, Panier
from shop.models import Produit, Photo

def panier(request):
    panier = PanierItem.objects.filter(user = request.user)
    temp = []
    for pro in panier:
        produitPho = pro.product.id
        produitPho2 = Photo.objects.get(produitId=produitPho)
        temp.append(produitPho2)

    item_number = panier.count()
    bool = False

    if item_number <= 0:
        bool = True

    context = {
        'item_number': item_number,
        'bool': bool,
        'temp': temp,
        'panier': panier,
    }
    return render(request, 'cart/pages/cart.html', context)

@login_required()
def add_to_cart_cos(request, id):
    # get the user profile
    user_profile = get_object_or_404(User, id=request.user.id)
    # filter products by id
    produit = Produit.objects.get(id=id)

    # create order associated with the user
    user_order, status = Panier.objects.get_or_create(user=user_profile, ordered=False)

    # create orderItem of the selected product
    order_item, status = PanierItem.objects.get_or_create(product=produit, user = user_profile, cart = user_order)
    order_item.save()

    messages.info(request, "Item added to cart.")
    return redirect('shop:cosmetique')

def add_to_cart_proInt(request, id):
    # get the user profile
    user_profile = get_object_or_404(User, id=request.user.id)
    # filter products by id
    produit = Produit.objects.get(id=id)

    # create order associated with the user
    user_order, status = Panier.objects.get_or_create(user=user_profile, ordered=False)

    # create orderItem of the selected product
    order_item, status = PanierItem.objects.get_or_create(product=produit, user = user_profile, cart = user_order)
    order_item.save()

    messages.info(request, "Item added to cart.")
    return redirect('shop:produitInterieur')

def add_to_cart_vet(request, id):
    # get the user profile
    user_profile = get_object_or_404(User, id=request.user.id)
    # filter products by id
    produit = Produit.objects.get(id=id)

    # create order associated with the user
    user_order, status = Panier.objects.get_or_create(user=user_profile, ordered=False)

    # create orderItem of the selected product
    order_item, status = PanierItem.objects.get_or_create(product=produit, user = user_profile, cart = user_order)
    order_item.save()

    messages.info(request, "Item added to cart.")
    return redirect('shop:vetements')

def delete_from_cart(request, item_id):
    item_to_delete = PanierItem.objects.get(pk=item_id)

    if item_to_delete.id > 0:
        item_to_delete.delete()
        messages.info(request, "Item has been removed.")
    return redirect(reverse('cart:panier'))