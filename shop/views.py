###############################################
# Import
###############################################
from django.shortcuts import render, redirect
from django.shortcuts import render

from shop.forms import PosteInsertVet, PosteInsertProInt, PosteInsertProCos, PosteInsertAtelier, PosteUpdateStockProCos, \
    PosteUpdateStockProInt, PosteUpdateStockVet, PosteInsertPhoto
from shop.models import Vetement, Produit, Cosmetique, ProduitInterieur, Prix, Atelier, Photo


def accueil(request):
    cosmetique = Cosmetique.objects.all()
    context = {
        'cosmetique': cosmetique,
    }
    return render(request, "shop/pages/accueil.html", context)


###############################################
## View Accueil Admin Test
###############################################
def accueilAdmin(request):
    context = {}
    return render(request, "shop/pages/accueilAdmin.html", context)


###############################################
## View Gestion de Stock Test
###############################################
def gestionStock(request):
    vetements = Vetement.objects.all()
    produitsInterieurs = ProduitInterieur.objects.all()
    produitsCosmetiques = Cosmetique.objects.all()
    return render(request, "shop/pages/gestionStock.html",
                  {'vetements': vetements, 'produitsInterieurs': produitsInterieurs,
                   'produitsCosmetiques': produitsCosmetiques})


###############################################
## View Gestion de produit Test
###############################################
def gestionProduit(request):
    vetementsGP = Vetement.objects.all()
    produitsInterieursGP = ProduitInterieur.objects.all()
    produitsCosmetiquesGP = Cosmetique.objects.all()
    return render(request, "shop/pages/gestionProduit.html",
                  {'vetementsGP': vetementsGP, 'produitsInterieursGP': produitsInterieursGP,
                   'produitsCosmetiquesGP': produitsCosmetiquesGP})


###############################################
## View Gestion d'atelier Test
###############################################
def gestionAtelier(request):
    atelier = Atelier.objects.all()
    return render(request, "shop/pages/gestionAtelier.html", {'atelier': atelier})


###############################################
## View Insertion Vetêments Test
###############################################
def insertionVetement(request):
    if request.method == "POST":
        formInsertVet = PosteInsertVet(request.POST)

        if formInsertVet.is_valid():
            formInsertVet = formInsertVet.save(commit=False)
            formInsertVet.author = request.user
            formInsertVet.save()

            return redirect('shop:insertionVetement')

    else:
        formInsertVet = PosteInsertVet()

    ## Insertion Photo
    if request.method == "POST":
        formInsertPhoto = PosteInsertPhoto(request.POST)

        if formInsertPhoto.is_valid():
            formInsertPhoto = formInsertPhoto.save(commit=False)
            formInsertPhoto.author = request.user
            formInsertPhoto.save()

            return redirect('shop:insertionVetement')

    else:
        formInsertVet = PosteInsertVet()
        formInsertPhoto = PosteInsertPhoto()

    return render(request, "shop/pages/insertionVetement.html",
                  {'formInsertVet': formInsertVet, 'formInsertPhoto': formInsertPhoto})


###############################################
## View Insertion Produit Intérieur Test
###############################################
def insertionProInt(request):
    if request.method == "POST":
        formInsertProInt = PosteInsertProInt(request.POST)

        if formInsertProInt.is_valid():
            formInsertProInt = formInsertProInt.save(commit=False)
            formInsertProInt.author = request.user
            formInsertProInt.save()

            return redirect('shop:insertionProInt')

    else:
        formInsertProInt = PosteInsertProInt()

    return render(request, "shop/pages/insertionProInt.html",
                  {'formInsertProInt': formInsertProInt})


###############################################
## View Insertion Produits Cosmétiques Test
###############################################
def insertionProCos(request):
    if request.method == "POST":
        formInsertProCos = PosteInsertProCos(request.POST)

        if formInsertProCos.is_valid():
            formInsertProCos = formInsertProCos.save(commit=False)
            formInsertProCos.author = request.user
            formInsertProCos.save()

            return redirect('shop:insertionProCos')

    else:
        formInsertProCos = PosteInsertProCos()

    return render(request, "shop/pages/insertionProCos.html",
                  {'formInsertProCos': formInsertProCos})


###############################################
## View Insertion Atelier Test
###############################################
def insertionAtelier(request):
    if request.method == "POST":
        formInsertAtelier = PosteInsertAtelier(request.POST)

        if formInsertAtelier.is_valid():
            formInsertAtelier = formInsertAtelier.save(commit=False)
            formInsertAtelier.author = request.user
            formInsertAtelier.save()

            return redirect('shop:insertionAtelier')

    else:
        formInsertAtelier = PosteInsertAtelier()

    return render(request, "shop/pages/insertionAtelier.html",
                  {'formInsertAtelier': formInsertAtelier})


### Update Vetêment
def updateVet(request, id):
    vetementUpdate = Vetement.objects.get(id=id)
    formUpdateVet = PosteInsertVet(request.POST or None, instance=vetementUpdate)
    if formUpdateVet.is_valid():
        formUpdateVet.save()
        return redirect('shop:gestionProduit')
    return render(request, "shop/pages/updateVet.html",
                  {'vetementUpdate': vetementUpdate, 'formUpdateVet': formUpdateVet})


### Update Produit Intérieur
def updateProInt(request, id):
    proIntUpdate = ProduitInterieur.objects.get(id=id)
    formUpdateProInt = PosteInsertProInt(request.POST or None, instance=proIntUpdate)
    if formUpdateProInt.is_valid():
        formUpdateProInt.save()
        return redirect('shop:gestionProduit')
    return render(request, "shop/pages/updateProInt.html",
                  {'proIntUpdate': proIntUpdate, 'formUpdateProInt': formUpdateProInt})


### Update Produit Cosmétique
def updateProCos(request, id):
    proCosUpdate = Cosmetique.objects.get(id=id)
    formUpdateProCos = PosteInsertProCos(request.POST or None, instance=proCosUpdate)
    if formUpdateProCos.is_valid():
        formUpdateProCos.save()
        return redirect('shop:gestionProduit')
    return render(request, "shop/pages/updateProCos.html",
                  {'proCosUpdate': proCosUpdate, 'formUpdateProCos': formUpdateProCos})


### Update Produit Cosmétique
def updateAtelier(request, id):
    atelierUpdate = Atelier.objects.get(id=id)
    formUpdateAtelier = PosteInsertAtelier(request.POST or None, instance=atelierUpdate)
    if formUpdateAtelier.is_valid():
        formUpdateAtelier.save()
        return redirect('shop:gestionAtelier')
    return render(request, "shop/pages/updateAtelier.html",
                  {'atelierUpdate': atelierUpdate, 'formUpdateAtelier': formUpdateAtelier})

### Update stock de Vetêment
def updateStockVet(request, id):
    stockVetementUpdate = Vetement.objects.get(id=id)
    formUpdateStockVet = PosteUpdateStockVet(request.POST or None, instance=stockVetementUpdate)
    if formUpdateStockVet.is_valid():
        formUpdateStockVet.save()
        return redirect('shop:gestionStock')
    return render(request, "shop/pages/updateStockVet.html",
                  {'stockVetementUpdate': stockVetementUpdate, 'formUpdateStockVet': formUpdateStockVet})


### Update stock de Produit Intérieur
def updateStockProInt(request, id):
    stockProIntUpdate = ProduitInterieur.objects.get(id=id)
    formUpdateStockProInt = PosteUpdateStockProInt(request.POST or None, instance=stockProIntUpdate)
    if formUpdateStockProInt.is_valid():
        formUpdateStockProInt.save()
        return redirect('shop:gestionStock')
    return render(request, "shop/pages/updateStockProInt.html",
                  {'stockProIntUpdate': stockProIntUpdate, 'formUpdateStockProInt': formUpdateStockProInt})


### Update stock de Produit Cosmétique
def updateStockProCos(request, id):
    stockProCosUpdate = Cosmetique.objects.get(id=id)
    formUpdateStockProCos = PosteUpdateStockProCos(request.POST or None, instance=stockProCosUpdate)
    if formUpdateStockProCos.is_valid():
        formUpdateStockProCos.save()
        return redirect('shop:gestionStock')
    return render(request, "shop/pages/updateStockProCos.html",
                  {'stockProCosUpdate': stockProCosUpdate, 'formUpdateStockProCos': formUpdateStockProCos})

### Détails Vetêments Admin
def adminVetDetails(request, id):
    detailsVet = Vetement.objects.get(id=id)
    return render(request, "shop/pages/adminVetDetails.html", {'detailsVet': detailsVet})


### Détails ProInt Admin
def adminProIntDetails(request, id):
    detailsProInt = ProduitInterieur.objects.get(id=id)
    return render(request, "shop/pages/adminProIntDetails.html", {'detailsProInt': detailsProInt})

### Détails ProCos Admin
def adminProCosDetails(request, id):
    detailsProCos = Cosmetique.objects.get(id=id)
    return render(request, "shop/pages/adminProCosDetails.html", {'detailsProCos': detailsProCos})

### Détails Atelier Admin
def adminAtelierDetails(request, id):
    detailsAtelier = Atelier.objects.get(id=id)
    return render(request, "shop/pages/adminAtelierDetails.html", {'detailsAtelier': detailsAtelier})


############################################

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
def vetement(request):
    vetements = Vetement.objects.all()
    sommesVet = Prix.objects.all()
    photVet = Photo.objects.all()

    context = {
        'photVet': photVet,
        'vetements': vetements,
        'sommesVet': sommesVet,
    }
    return render(request, 'shop/pages/vetements.html', context)


def produitInterieur(request):
    produitInt = ProduitInterieur.objects.all()
    sommesProInt = Prix.objects.all()
    photos = Photo.objects.all()

    context = {
        'photos': photos,
        'produitInt': produitInt,
        'sommesProInt': sommesProInt,
    }
    return render(request, 'shop/pages/produitInterieur.html', context)


def cosmetique(request):
    cosmetiques = Cosmetique.objects.all()
    sommesCos = Prix.objects.all()
    photos = Photo.objects.all()
    fav = bool
    context = {
        'photos': photos,
        'cosmetiques': cosmetiques,
        'sommesCos': sommesCos,
        'fav': fav,
    }
    if cosmetiques.filter(favoris=request.user.pk):
        fav = True
    return render(request, 'shop/pages/cosmetique.html', context)


###############################################
# Detail produit
###############################################
def detailsVet(request, id):
    vetements = Vetement.objects.get(id=id)
    somVet = Prix.objects.get(produit=id)
    photVet = Photo.objects.get(produitId=id)

    context = {
        'vetements': vetements,
        'somVet': somVet,
        'photVet': photVet,
    }
    return render(request, 'shop/pages/detailsVet.html', context)


def detailsProInt(request, id):
    produitInt = ProduitInterieur.objects.get(id=id)
    sommesProInt = Prix.objects.get(produit=id)
    phoProInt = Photo.objects.get(produitId=id)

    context = {
        'phoProInt': phoProInt,
        'produitInt': produitInt,
        'sommesProInt': sommesProInt,
    }
    return render(request, 'shop/pages/detailsProInt.html', context)


def detailsCos(request, id):
    cosmetiques = Cosmetique.objects.get(id=id)
    sommesCos = Prix.objects.get(produit=id)
    phoCos = Photo.objects.get(produitId=id)

    context = {
        'phoCos': phoCos,
        'cosmetiques': cosmetiques,
        'sommesCos': sommesCos,
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
