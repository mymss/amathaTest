
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.shortcuts import render

from accounts.models import Client
from shop.forms import PosteInsertVet, PosteInsertProInt, PosteInsertProCos, PosteInsertAtelier, PosteUpdateStockProCos, \
    PosteUpdateStockProInt, PosteUpdateStockVet
from shop.models import Vetement, Produit, Cosmetique, ProduitInterieur, Prix, Atelier, Commande, \
    LigneProduitCommande, LigneAtelierCommande


@login_required
def header(request):
    username = User.username
    context = {
        'username': username,
    }
    return render(request, 'shop/layouts/header.html', context)


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
    paginator = Paginator(cosmetiques, 6)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    num = request.user.pk
    qsProduitsFavs = Cosmetique.objects.filter(favoris=num)

    cosFav = []
    for produit in qsProduitsFavs:
        cosFav.append(Cosmetique.objects.get(produit_ptr=produit.pk))

    context = {
        'cosmetiques': page_obj,
        'sommesCos': sommesCos,
        'cosFav': cosFav,
    }

    return render(request, 'shop/pages/cosmetique.html', context)


def vetement(request):
    vetements = Vetement.objects.all()
    sommesVet = Prix.objects.all()
    paginator = Paginator(vetements, 6)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    num = request.user.pk
    qsVetementFavs = Vetement.objects.filter(favoris=num)

    vetFav = []
    for produit in qsVetementFavs:
        vetFav.append(Vetement.objects.get(produit_ptr=produit.pk))

    context = {
        'vetements': page_obj,
        'sommesVet': sommesVet,
        'vetFav': vetFav,
    }

    return render(request, 'shop/pages/vetements.html', context)


def produitInterieur(request):
    produitInt = ProduitInterieur.objects.all()
    sommesProInt = Prix.objects.all()
    paginator = Paginator(produitInt, 6)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    num = request.user.pk
    qsProduitsFavs = ProduitInterieur.objects.filter(favoris=num)

    proIntFav = []
    for produit in qsProduitsFavs:
        proIntFav.append(ProduitInterieur.objects.get(produit_ptr=produit.pk))

    context = {
        'produitInt': page_obj,
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
    paginator = Paginator(ateliers, 6)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    num = request.user.pk
    qsAtelierFavs =Atelier.objects.filter(favorisAtelier=num)

    ateFav = []
    for atelier in qsAtelierFavs:
        ateFav.append(Atelier.objects.get(id = atelier.pk))

    context = {
        'ateliers': page_obj,
        'ateFav': ateFav,
    }
    return render(request, 'shop/pages/atelier.html', context)


def detailsAtelier(request, id):
    atel = Atelier.objects.get(id=id)

    num = request.user.pk
    qsAtelierFavs = Atelier.objects.filter(favorisAtelier=num)

    ateFav = []
    for atelier in qsAtelierFavs:
        ateFav.append(Atelier.objects.get(id=atelier.pk))
    context = {
        'atel': atel,
        'ateFav':ateFav,
    }
    return render(request, 'shop/pages/detailsAtelier.html', context)

###############################################
# Page Commande + Détail commande
###############################################


def commande(request):
    infos = request.user.client
    commandes = Commande.objects.filter(clientId=infos.id)
    paginator = Paginator(commandes, 6)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    totalProduit = 0
    totalAtelier = 0
    nmbrElementProduit = 0
    nmbrElementAtelier = 0
    listeProduit = []
    listeAtelier = []
    totalCommande = []
    listeNbrProduit = []
    listeNbrAtelier = []

    for com in commandes:
        ligneProCom = LigneProduitCommande.objects.filter(commande=com)
        ligneAteCom = LigneAtelierCommande.objects.filter(commande=com)
        totalProduit = 0
        totalAtelier = 0
        nmbrElementProduit = 0
        nmbrElementAtelier = 0
        for pro in ligneProCom:
            montant = Prix.objects.get(produit=pro.produit)
            totalProduit += montant.montant * pro.quantite
            nmbrElementProduit += 1
        listeNbrProduit.append(nmbrElementProduit)
        # listeProduit.append(totalProduit)
        for ate in ligneAteCom:
            atelier = Atelier.objects.get(id=ate.atelier.id)
            totalAtelier += atelier.prix * ate.nbrPersonne
            nmbrElementAtelier += 1
        listeNbrAtelier.append(nmbrElementAtelier)
        # listeAtelier.append(totalAtelier)
        totalCommande.append(totalAtelier + totalProduit)

    context = {
        'totalProduit': totalProduit,
        'commandes': commandes,
        'listeProduit': listeProduit,
        'listeAtelier': listeAtelier,
        'totalCommande': totalCommande,
        'listeNbrAtelier': listeNbrAtelier,
        'listeNbrProduit': listeNbrProduit,
        'commandesPag': page_obj
    }
    return render(request, 'shop/pages/commande.html', context)


def detailsCommande(request, id, ):
    detCommande = Commande.objects.get(id=id)
    ligneProCom = LigneProduitCommande.objects.filter(commande=id)
    ligneAteCom = LigneAtelierCommande.objects.filter(commande=id)

    totalProduit = 0
    totalAtelier = 0
    totalFinal = 0

    for pro in ligneProCom:
        montant = Prix.objects.get(produit=pro.produit)
        totalProduit += montant.montant * pro.quantite
        prix = Prix.objects.all()

    for ate in ligneAteCom:
        atelier = Atelier.objects.get(id=ate.atelier.id)
        totalAtelier += atelier.prix * ate.nbrPersonne
    totalFinal = totalAtelier + totalProduit

    context = {
        'detCommande': detCommande,
        'ligneProCom': ligneProCom,
        'ligneAteCom': ligneAteCom,
        'prix': prix,
        'totalAtelier': totalAtelier,
        'totalProduit': totalProduit,
        'totalFinal': totalFinal,
    }
    return render(request, 'shop/pages/detailsCommande.html', context)

###############################################
# Recherche Produit
###############################################

def searchProduit(request):
    if request.method == "POST":
        searchedProduit = request.POST['searchedProduit']
        produits = Produit.objects.filter(nom__contains=searchedProduit)

        cosmetiques = Cosmetique.objects.all()
        produitsInt = ProduitInterieur.objects.all()
        vetements = Vetement.objects.all()
        prix = Prix.objects.all()

        num = request.user.pk
        qsProduitFavs = Cosmetique.objects.filter(favoris=num)

        produitsFav = []

        for pro in qsProduitFavs:
            produitsFav.append(Cosmetique.objects.get(produit_ptr=pro.pk))

        context = {
            'searchedProduit': searchedProduit,
            'produits': produits,
            'cosmetiques': cosmetiques,
            'produitsInt': produitsInt,
            'vetements': vetements,
            'prix': prix,
            'produitsFav': produitsFav,
        }
        return render(request, "shop/pages/searchProduit.html", context)

    else:
        return render(request, "shop/pages/searchProduit.html")

###############################################
# Page Qui Sommes-Nous!?
###############################################
def quiSommesNous(request):
    produit = Produit.objects.all()
    context={
        'produit': produit,
    }
    return render(request, "shop/pages/quiSommesNous.html",context)