from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from cart.models import PanierItem, Panier
from shop.models import Produit, Atelier


def panier(request):
    panier = Panier.objects.filter(user=request.user)
    panierItems = PanierItem.objects.filter(user=request.user)

    item_number = panierItems.count()
    bool = False

    if item_number <= 0:
        bool = True

    context = {
        'item_number': item_number,
        'bool': bool,
        'panierItems': panierItems,
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
    order_item, status = PanierItem.objects.get_or_create(product=produit, user=user_profile, cart=user_order)
    order_item.save()

    messages.info(request, "Item added to cart.")
    return redirect('shop:cosmetique')

@login_required()
def add_to_cart_proInt(request, id):
    # get the user profile
    user_profile = get_object_or_404(User, id=request.user.id)
    # filter products by id
    produit = Produit.objects.get(id=id)

    # create order associated with the user
    user_order, status = Panier.objects.get_or_create(user=user_profile, ordered=False)

    # create orderItem of the selected product
    order_item, status = PanierItem.objects.get_or_create(product=produit, user=user_profile, cart=user_order)
    order_item.save()

    messages.info(request, "Item added to cart.")
    return redirect('shop:produitInterieur')

@login_required()
def add_to_cart_vet(request, id):
    # get the user profile
    user_profile = get_object_or_404(User, id=request.user.id)
    # filter products by id
    produit = Produit.objects.get(id=id)

    # create order associated with the user
    user_order, status = Panier.objects.get_or_create(user=user_profile, ordered=False)

    # create orderItem of the selected product
    order_item, status = PanierItem.objects.get_or_create(product=produit, user=user_profile, cart=user_order)
    order_item.save()

    messages.info(request, "Item added to cart.")
    return redirect('shop:vetements')

@login_required()
def add_to_cart_atelier(request, id):
    # get the user profile
    user_profile = get_object_or_404(User, id=request.user.id)
    # filter atelier by id
    atelier = Atelier.objects.get(id=id)

    # create order associated with the user
    user_order, status = Panier.objects.get_or_create(user=user_profile, ordered=False)

    # create orderItem of the selected product
    order_item, status = PanierItem.objects.get_or_create(atelier=atelier, user=user_profile, cart=user_order)
    order_item.save()

    messages.info(request, "Item added to cart.")
    return redirect('shop:atelier')


def update_quantity_more(request, item_id):
    quantity_to_update = PanierItem.objects.get(pk=item_id)
    print(quantity_to_update.atelier)

    if quantity_to_update.atelier :
        atelierInst = Atelier.objects.get(id=quantity_to_update.atelier.id)
        if quantity_to_update.quantity <= atelierInst.nbrPersonneMax:
            quantity_to_update.quantity += 1
            quantity_to_update.save()
        else:
            messages.info(request, "Max stock")

    elif quantity_to_update.product:
        productInst = Produit.objects.get(id=quantity_to_update.product.id)
        if quantity_to_update.quantity <= productInst.stockDisponible:
            quantity_to_update.quantity += 1
            quantity_to_update.save()
        else:
            messages.info(request, "Max stock")

    return redirect(reverse('cart:panier'))


def update_quantity_less(request, item_id):
    quantity_to_update = PanierItem.objects.get(pk=item_id)

    if quantity_to_update.quantity > 1:
        quantity_to_update.quantity -= 1
        quantity_to_update.save()
    else:
        delete_from_cart(request, item_id)

    return redirect(reverse('cart:panier'))


def delete_from_cart(request, item_id):
    item_to_delete = PanierItem.objects.get(pk=item_id)
    cart = Panier.objects.get(user=request.user)

    if item_to_delete.id > 0:
        item_to_delete.delete()
        cart.total_price = cart.total_price - item_to_delete.price
        cart.save()
        messages.info(request, "Item has been removed.")
    return redirect(reverse('cart:panier'))


#################################################################################################
########## Bar de Recherche #############
@login_required()
def add_to_cart_produit_search(request, id):
    # get the user profile
    user_profile = get_object_or_404(User, id=request.user.id)
    # filter products by id
    produit = Produit.objects.get(id=id)

    # create order associated with the user
    user_order, status = Panier.objects.get_or_create(user=user_profile, ordered=False)

    # create orderItem of the selected product
    order_item, status = PanierItem.objects.get_or_create(product=produit, user=user_profile, cart=user_order)
    order_item.save()

    messages.info(request, "Item added to cart.")
    return redirect('shop:accueil')
