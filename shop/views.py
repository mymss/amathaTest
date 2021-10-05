
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render

from accounts.models import Client
from shop.forms import PosteInsertVet, PosteInsertProInt, PosteInsertProCos, PosteInsertAtelier, PosteUpdateStockProCos, \
    PosteUpdateStockProInt, PosteUpdateStockVet
from shop.models import Vetement, Produit, Cosmetique, ProduitInterieur, Prix, Atelier, Commande, \
    LigneProduitCommande, LigneAtelierCommande


@login_required
def header(request):
    infos = request.user.client
    context = {
        'infos': infos,
    }
    return render(request, 'shop/layouts/header', context)


def accueil(request):
    produits = Produit.objects.all()[:4]
    prix = Prix.objects.all()

    vetements = Vetement.objects.all()
    produitsInterieurs = ProduitInterieur.objects.all()
    produitsCosmetiques = Cosmetique.objects.all()

    context = {
        'produits': produits,
        'prix': prix,
        'vetements': vetements,
        'produitsInterieurs': produitsInterieurs,
        'produitsCosmetiques': produitsCosmetiques,
    }
    return render(request, "shop/pages/accueil.html", context)



def vetements(request):
    vetement = Vetement.objects.all()
    return render(request, '../../shop/templates/shop/layouts/accordionStock.html', {'vetement': vetement})


def produitsInterieurs(request):
    produitInterieur = ProduitInterieur.objects.all()
    return render(request, '../../shop/templates/shop/layouts/accordionStock.html',
                  {'produitInterieur': produitInterieur})


def produitsCosmetiques(request):
    cosmetique = Cosmetique.objects.all()
    return render(request, '../../shop/templates/shop/layouts/accordionStock.html',
                  {'cosmetique': cosmetique})


###############################################
# Page Produit
###############################################
def cosmetique(request):
    cosmetiques = Cosmetique.objects.all()
    sommesCos = Prix.objects.all()

    num = request.user.pk
    qsProduitsFavs = Cosmetique.objects.filter(favoris=num)

    cosFav = []
    for produit in qsProduitsFavs:
        cosFav.append(Cosmetique.objects.get(produit_ptr=produit.pk))

    context = {
        'cosmetiques': cosmetiques,
        'sommesCos': sommesCos,
        'cosFav': cosFav,
    }

    return render(request, 'shop/pages/cosmetique.html', context)


def vetement(request):
    vetements = Vetement.objects.all()
    sommesVet = Prix.objects.all()

    num = request.user.pk
    qsVetementFavs = Vetement.objects.filter(favoris=num)

    vetFav = []
    for produit in qsVetementFavs:
        vetFav.append(Vetement.objects.get(produit_ptr=produit.pk))

    context = {
        'vetements': vetements,
        'sommesVet': sommesVet,
        'vetFav': vetFav,
    }

    return render(request, 'shop/pages/vetements.html', context)


def produitInterieur(request):
    produitInt = ProduitInterieur.objects.all()
    sommesProInt = Prix.objects.all()

    num = request.user.pk
    qsProduitsFavs = ProduitInterieur.objects.filter(favoris=num)

    proIntFav = []
    for produit in qsProduitsFavs:
        proIntFav.append(ProduitInterieur.objects.get(produit_ptr=produit.pk))

    context = {
        'produitInt': produitInt,
        'sommesProInt': sommesProInt,
        'proIntFav': proIntFav,
    }
    return render(request, 'shop/pages/produitInterieur.html', context)


###############################################
# Detail produit
###############################################
def detailsVet(request, id):
    vetements = Vetement.objects.get(id=id)
    somVet = Prix.objects.get(produit=id)

    num = request.user.pk
    qsProduitsFavs = Vetement.objects.filter(favoris=num)

    vetFav = []
    for produit in qsProduitsFavs:
        vetFav.append(Vetement.objects.get(produit_ptr=produit.pk))

    context = {
        'vetements': vetements,
        'somVet': somVet,
        'vetFav': vetFav,
    }
    return render(request, 'shop/pages/detailsVet.html', context)


def detailsProInt(request, id):
    produitInt = ProduitInterieur.objects.get(id=id)
    sommesProInt = Prix.objects.get(produit=id)

    num = request.user.pk
    qsProduitsFavs = ProduitInterieur.objects.filter(favoris=num)

    proIntFav = []
    for produit in qsProduitsFavs:
        proIntFav.append(ProduitInterieur.objects.get(produit_ptr=produit.pk))

    context = {
        'produitInt': produitInt,
        'sommesProInt': sommesProInt,
        'proIntFav': proIntFav,
    }
    return render(request, 'shop/pages/detailsProInt.html', context)


def detailsCos(request, id):
    cosmetiques = Cosmetique.objects.get(id=id)
    sommesCos = Prix.objects.get(produit=id)

    num = request.user.pk
    qsProduitsFavs = Cosmetique.objects.filter(favoris=num)

    cosFav = []
    for produit in qsProduitsFavs:
        cosFav.append(Cosmetique.objects.get(produit_ptr=produit.pk))

    context = {
        'cosmetiques': cosmetiques,
        'sommesCos': sommesCos,
        'cosFav': cosFav,
    }
    return render(request, 'shop/pages/detailsCos.html', context)


###############################################
# Page Atelier
###############################################
def atelier(request):
    ateliers = Atelier.objects.all()
    context = {
        'ateliers': ateliers,
    }
    return render(request, 'shop/pages/atelier.html', context)


def detailsAtelier(request, id):
    atel = Atelier.objects.get(id=id)
    context = {
        'atel': atel,
    }
    return render(request, 'shop/pages/detailsAtelier.html', context)


###############################################
# Page Commande + Détail commande
###############################################


def commande(request):
    infos = request.user.client
    commandes = Commande.objects.filter(clientId_id=request.user.client.id)
    context={
        'commandes': commandes,
    }
    return render(request, 'shop/pages/commande.html', context)


# def calculCommande(idCom):
#     # Commnde Id
#     commande_id = Commande.objects.get(id=idCom)
#     # Produit
#     ligneProduit = LigneProduitCommande.objects.filter(produit__commande__ligneproduitcommande=commande_id)
#     montant = Prix.objects.filter(produit__ligneproduitcommande__commande_id=commande_id)
#     comPro = Commande.objects.filter(clientId__commande=commande_id)
#     totalComProduit = 0
#     # Atelier
#     comAte = Commande.objects.filter(clientId__commande= commande_id)
#     ligneAtelier = LigneAtelierCommande.objects.filter(commande__clientId__commande=commande_id)
#     totalComAtelier = 0
#     total = []
#
#     for lignepro in ligneProduit:
#         for pri in montant:
#             for pro in comPro:
#                 if commande_id == lignepro.commande:
#                     totalComProduit += pri.montant * lignepro.quantite
#
#     for ligneate in ligneAtelier:
#         for ate in comAte:
#             totalComAtelier += ate.prix * ligneate.nbrPersonne
#
#     total.append(totalComAtelier + totalComProduit)
#     for tot in total:
#         tot.
#     return
#

def detailsCommande(request, id):
    detailsCommande = Commande.objects.get(id=id)
    ligneProCom = LigneProduitCommande.objects.filter(commande=id)
    ligneAteCom = LigneAtelierCommande.objects.filter(commande=id)
    prix = Prix.objects.all()
    # calculeTotal = {{methods.calculePrixTotal(prix.all(), ligneProCom.all())}}
    context = {
        'detailsCommande': detailsCommande,
        'ligneProCom': ligneProCom,
        'ligneAteCom': ligneAteCom,
        'prix': prix,
    }
    return render(request, 'shop/pages/detailsCommande.html', context)
