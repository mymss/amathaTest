
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.models import Client
from shop.forms import PosteInsertVet, PosteInsertProInt, PosteInsertProCos, PosteInsertAtelier, PosteUpdateStockProCos, \
    PosteUpdateStockProInt, PosteUpdateStockVet, PosteUpdatePrix
from shop.models import Vetement, Produit, Cosmetique, ProduitInterieur, Prix, Atelier, Commande, \
    LigneProduitCommande, LigneAtelierCommande

# Create your views here.



###############################################
## View Accueil Admin Test
###############################################
def accueilAdmin(request):
    context = {}
    return render(request, "administration/pages/accueilAdmin.html", context)


###############################################
## View Gestion de Stock Test
###############################################
def gestionStock(request):
    vetements = Vetement.objects.all()
    produitsInterieurs = ProduitInterieur.objects.all()
    produitsCosmetiques = Cosmetique.objects.all()
    return render(request, "administration/pages/gestionStock.html",
                  {'vetements': vetements, 'produitsInterieurs': produitsInterieurs,
                   'produitsCosmetiques': produitsCosmetiques})


###############################################
## View Gestion de produit Test
###############################################
def gestionProduit(request):
    produit = Produit.objects.all()
    vetementsGP = Vetement.objects.all()
    prix = Prix.objects.all()
    produitsInterieursGP = ProduitInterieur.objects.all()
    produitsCosmetiquesGP = Cosmetique.objects.all()
    return render(request, "administration/pages/gestionProduit.html",
                  {'vetementsGP': vetementsGP, 'produitsInterieursGP': produitsInterieursGP,
                   'produitsCosmetiquesGP': produitsCosmetiquesGP, 'prix': prix})


###############################################
## View Gestion d'atelier Test
###############################################
def gestionAtelier(request):
    atelier = Atelier.objects.all()
    return render(request, "administration/pages/gestionAtelier.html", {'atelier': atelier})


###############################################
## View Gestion de client Test
###############################################
def gestionClient(request):
    client = Client.objects.all()
    return render(request, "administration/pages/gestionClient.html", {'client': client})


###############################################
## View Gestion de client Test
###############################################
def gestionCommande(request):
    commande = Commande.objects.all()
    return render(request, "administration/pages/gestionCommande.html", {'commande': commande})



### Détails Vetêments Admin
def adminVetDetails(request, id):
    detailsVet = Vetement.objects.get(id=id)
    return render(request, "administration/pages/adminVetDetails.html", {'detailsVet': detailsVet})


### Détails ProInt Admin
def adminProIntDetails(request, id):
    detailsProInt = ProduitInterieur.objects.get(id=id)
    return render(request, "administration/pages/adminProIntDetails.html", {'detailsProInt': detailsProInt})


### Détails ProCos Admin
def adminProCosDetails(request, id):
    detailsProCos = Cosmetique.objects.get(id=id)
    return render(request, "administration/pages/adminProCosDetails.html", {'detailsProCos': detailsProCos})


### Détails Atelier Admin
def adminAtelierDetails(request, id):
    detailsAtelier = Atelier.objects.get(id=id)
    return render(request, "administration/pages/adminAtelierDetails.html", {'detailsAtelier': detailsAtelier})


### Détails client Admin
def adminClientDetails(request, id):
    detailsClient = Client.objects.get(id=id)
    commande = Commande.objects.filter(clientId=id)
    context = {
        'detailsClient': detailsClient,
        'commande': commande,
    }
    return render(request, "administration/pages/adminClientDetails.html", context)


### Détails commande Admin
def adminCommandeDetails(request, id):
    detailsCommande = Commande.objects.get(id=id)
    ligneCom = LigneProduitCommande.objects.filter(commande=id)
    context = {
        'detailsCommande': detailsCommande,
        'ligneCom': ligneCom,
    }
    return render(request, "administration/pages/adminCommandeDetails.html", context)

##############################################
## View Insertion Vetêments Test
###############################################
def insertionVetement(request):
    if request.method == "POST":
        formInsertVet = PosteInsertVet(request.POST)

        if formInsertVet.is_valid():
            formInsertVet = formInsertVet.save(commit=False)
            formInsertVet.author = request.user
            formInsertVet.save()

            return redirect('administration:insertionVetement')

    else:
        formInsertVet = PosteInsertVet()


    return render(request, "administration/pages/insertionVetement.html",
                  {'formInsertVet': formInsertVet})


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

            return redirect('administration:insertionProInt')

    else:
        formInsertProInt = PosteInsertProInt()

    return render(request, "administration/pages/insertionProInt.html",
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

            return redirect('administration:insertionProCos')

    else:
        formInsertProCos = PosteInsertProCos()

    return render(request, "administration/pages/insertionProCos.html",
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

            return redirect('administration:insertionAtelier')

    else:
        formInsertAtelier = PosteInsertAtelier()

    return render(request, "administration/pages/insertionAtelier.html",
                  {'formInsertAtelier': formInsertAtelier})



### Update Vetêment
def updateVet(request, id):
    vetementUpdate = Vetement.objects.get(id=id)
    formUpdateVet = PosteInsertVet(request.POST or None, instance=vetementUpdate)
    if formUpdateVet.is_valid():
        formUpdateVet.save()
        return redirect('shop:gestionProduit')
    return render(request, "administration/pages/updateVet.html",
                  {'vetementUpdate': vetementUpdate, 'formUpdateVet': formUpdateVet})


### Update Produit Intérieur
def updateProInt(request, id):
    proIntUpdate = ProduitInterieur.objects.get(id=id)
    formUpdateProInt = PosteInsertProInt(request.POST or None, instance=proIntUpdate)
    if formUpdateProInt.is_valid():
        formUpdateProInt.save()
        return redirect('administration:gestionProduit')
    return render(request, "administration/pages/updateProInt.html",
                  {'proIntUpdate': proIntUpdate, 'formUpdateProInt': formUpdateProInt})


### Update Produit Cosmétique
def updateProCos(request, id):
    proCosUpdate = Cosmetique.objects.get(id=id)
    formUpdateProCos = PosteInsertProCos(request.POST or None, instance=proCosUpdate)
    if formUpdateProCos.is_valid():
        formUpdateProCos.save()
        return redirect('administration:gestionProduit')
    return render(request, "administration/pages/updateProCos.html",
                  {'proCosUpdate': proCosUpdate, 'formUpdateProCos': formUpdateProCos})

## Update Prix
def updatePrix(request, id):
    produit = Produit.objects.get(id=id)
    prixUpdate = Prix.objects.get(produit=produit.id)
    formUpdatePrix = PosteUpdatePrix(request.POST or None, instance=prixUpdate)
    if formUpdatePrix.is_valid():
        formUpdatePrix.save()
        return redirect('administration:gestionProduit')
    return render(request, "administration/pages/updatePrix.html",
                  {'prixUpdate': prixUpdate, 'formUpdatePrix': formUpdatePrix})



### Update Produit Cosmétique
def updateAtelier(request, id):
    atelierUpdate = Atelier.objects.get(id=id)
    formUpdateAtelier = PosteInsertAtelier(request.POST or None, instance=atelierUpdate)
    if formUpdateAtelier.is_valid():
        formUpdateAtelier.save()
        return redirect('administration:gestionAtelier')
    return render(request, "administration/pages/updateAtelier.html",
                  {'atelierUpdate': atelierUpdate, 'formUpdateAtelier': formUpdateAtelier})


### Update stock de Vetêment
def updateStockVet(request, id):
    stockVetementUpdate = Vetement.objects.get(id=id)
    formUpdateStockVet = PosteUpdateStockVet(request.POST or None, instance=stockVetementUpdate)
    if formUpdateStockVet.is_valid():
        formUpdateStockVet.save()
        return redirect('administration:gestionStock')
    return render(request, "administration/pages/updateStockVet.html",
                  {'stockVetementUpdate': stockVetementUpdate, 'formUpdateStockVet': formUpdateStockVet})


### Update stock de Produit Intérieur
def updateStockProInt(request, id):
    stockProIntUpdate = ProduitInterieur.objects.get(id=id)
    formUpdateStockProInt = PosteUpdateStockProInt(request.POST or None, instance=stockProIntUpdate)
    if formUpdateStockProInt.is_valid():
        formUpdateStockProInt.save()
        return redirect('administration:gestionStock')
    return render(request, "administration/pages/updateStockProInt.html",
                  {'stockProIntUpdate': stockProIntUpdate, 'formUpdateStockProInt': formUpdateStockProInt})


### Update stock de Produit Cosmétique
def updateStockProCos(request, id):
    stockProCosUpdate = Cosmetique.objects.get(id=id)
    formUpdateStockProCos = PosteUpdateStockProCos(request.POST or None, instance=stockProCosUpdate)
    if formUpdateStockProCos.is_valid():
        formUpdateStockProCos.save()
        return redirect('administration:gestionStock')
    return render(request, "administration/pages/updateStockProCos.html",
                  {'stockProCosUpdate': stockProCosUpdate, 'formUpdateStockProCos': formUpdateStockProCos})

