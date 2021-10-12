from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.models import Client
from shop.forms import PosteInsertVet, PosteInsertProInt, PosteInsertProCos, PosteInsertAtelier, PosteUpdateStockProCos, \
    PosteUpdateStockProInt, PosteUpdateStockVet, PosteUpdatePrix, PosteDesativerClient
from shop.models import Vetement, Produit, Cosmetique, ProduitInterieur, Prix, Atelier, Commande, \
    LigneProduitCommande, LigneAtelierCommande


# Create your views here.


###############################################
## View Accueil Admin Test
###############################################
def accueilAdmin(request):
    context = {}
    if request.user.is_superuser:
        return render(request, "administration/pages/accueilAdmin.html", context)
    else:
        return render(request, "shop/pages/accueil.html", context)


###############################################
## View Gestion de Stock Test
###############################################
def gestionStock(request):
    vetements = Vetement.objects.all()
    produitsInterieurs = ProduitInterieur.objects.all()
    produitsCosmetiques = Cosmetique.objects.all()

    if request.user.is_superuser:
        return render(request, "administration/pages/gestionStock.html",
                      {'vetements': vetements, 'produitsInterieurs': produitsInterieurs,
                       'produitsCosmetiques': produitsCosmetiques})
    else:
        return render(request, "shop/pages/accueil.html")


###############################################
## View Gestion de produit Test
###############################################
def gestionProduit(request):
    produit = Produit.objects.all()
    vetementsGP = Vetement.objects.all()
    prix = Prix.objects.all()
    produitsInterieursGP = ProduitInterieur.objects.all()
    produitsCosmetiquesGP = Cosmetique.objects.all()

    if request.user.is_superuser:
        return render(request, "administration/pages/gestionProduit.html",
                      {'vetementsGP': vetementsGP, 'produitsInterieursGP': produitsInterieursGP,
                       'produitsCosmetiquesGP': produitsCosmetiquesGP, 'prix': prix})
    else:
        return render(request, "shop/pages/accueil.html")


###############################################
## View Gestion d'atelier Test
###############################################
def gestionAtelier(request):
    atelier = Atelier.objects.all()

    if request.user.is_superuser:
        return render(request, "administration/pages/gestionAtelier.html", {'atelier': atelier})
    else:
        return render(request, "shop/pages/accueil.html")


###############################################
## View Gestion de client Test
###############################################
def gestionClient(request):
    client = Client.objects.all()

    if request.user.is_superuser:
        return render(request, "administration/pages/gestionClient.html", {'client': client})
    else:
        return render(request, "shop/pages/accueil.html")


###############################################
## View Gestion de client Test
###############################################
def gestionCommande(request):
    commandes = Commande.objects.all()
    totalProduit = 0
    totalAtelier = 0
    listeProduit = []
    listeAtelier = []
    totalCommande = []

    for com in commandes:
        ligneProCom = LigneProduitCommande.objects.filter(commande=com)
        ligneAteCom = LigneAtelierCommande.objects.filter(commande=com)
        totalProduit = 0
        totalAtelier = 0
        for pro in ligneProCom:
            montant = Prix.objects.get(produit=pro.produit)
            totalProduit += montant.montant * pro.quantite
        listeProduit.append(totalProduit)
        for ate in ligneAteCom:
            atelier = Atelier.objects.get(id=ate.atelier.id)
            totalAtelier += atelier.prix * ate.nbrPersonne
        listeAtelier.append(totalAtelier)
        totalCommande.append(totalAtelier + totalProduit)

    context = {
        'totalProduit': totalProduit,
        'commandes': commandes,
        'listeProduit': listeProduit,
        'listeAtelier': listeAtelier,
        'totalCommande': totalCommande,
    }

    if request.user.is_superuser:
        return render(request, "administration/pages/gestionCommande.html", context)
    else:
        return render(request, "shop/pages/accueil.html")


### Détails Vetêments Admin
def adminVetDetails(request, id):
    detailsVet = Vetement.objects.get(id=id)

    if request.user.is_superuser:
        return render(request, "administration/pages/adminVetDetails.html", {'detailsVet': detailsVet})
    else:
        return render(request, "shop/pages/accueil.html")


### Détails ProInt Admin
def adminProIntDetails(request, id):
    detailsProInt = ProduitInterieur.objects.get(id=id)

    if request.user.is_superuser:
        return render(request, "administration/pages/adminProIntDetails.html", {'detailsProInt': detailsProInt})
    else:
        return render(request, "shop/pages/accueil.html")


### Détails ProCos Admin
def adminProCosDetails(request, id):
    detailsProCos = Cosmetique.objects.get(id=id)

    if request.user.is_superuser:
        return render(request, "administration/pages/adminProCosDetails.html", {'detailsProCos': detailsProCos})
    else:
        return render(request, "shop/pages/accueil.html")


### Détails Atelier Admin
def adminAtelierDetails(request, id):
    detailsAtelier = Atelier.objects.get(id=id)

    if request.user.is_superuser:
        return render(request, "administration/pages/adminAtelierDetails.html", {'detailsAtelier': detailsAtelier})
    else:
        return render(request, "shop/pages/accueil.html")


### Détails client Admin
def adminClientDetails(request, id):
    detailsClient = Client.objects.get(id=id)
    commandes = Commande.objects.filter(clientId=id)
    totalProduit = 0
    totalAtelier = 0
    listeProduit = []
    listeAtelier = []
    totalCommande = []

    for com in commandes:
        ligneProCom = LigneProduitCommande.objects.filter(commande=com)
        ligneAteCom = LigneAtelierCommande.objects.filter(commande=com)
        totalProduit = 0
        totalAtelier = 0
        for pro in ligneProCom:
            montant = Prix.objects.get(produit=pro.produit)
            totalProduit += montant.montant * pro.quantite
        listeProduit.append(totalProduit)
        for ate in ligneAteCom:
            atelier = Atelier.objects.get(id=ate.atelier.id)
            totalAtelier += atelier.prix * ate.nbrPersonne
        listeAtelier.append(totalAtelier)
        totalCommande.append(totalAtelier + totalProduit)

    context = {
        'detailsClient': detailsClient,
        'totalProduit': totalProduit,
        'commandes': commandes,
        'listeProduit': listeProduit,
        'listeAtelier': listeAtelier,
        'totalCommande': totalCommande,
    }

    if request.user.is_superuser:
        return render(request, "administration/pages/adminClientDetails.html", context)
    else:
        return render(request, "shop/pages/accueil.html")


### Détails commande Admin
def adminCommandeDetails(request, id):
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

    if request.user.is_superuser:
        return render(request, "administration/pages/adminCommandeDetails.html", context)
    else:
        return render(request, "shop/pages/accueil.html")


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

    if request.user.is_superuser:
        return render(request, "administration/pages/insertionVetement.html",
                      {'formInsertVet': formInsertVet})
    else:
        return render(request, "shop/pages/accueil.html")


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

    if request.user.is_superuser:
        return render(request, "administration/pages/insertionProInt.html",
                      {'formInsertProInt': formInsertProInt})
    else:
        return render(request, "shop/pages/accueil.html")


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

    if request.user.is_superuser:
        return render(request, "administration/pages/insertionProCos.html",
                      {'formInsertProCos': formInsertProCos})
    else:
        return render(request, "shop/pages/accueil.html")


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

    if request.user.is_superuser:
        return render(request, "administration/pages/insertionAtelier.html",
                      {'formInsertAtelier': formInsertAtelier})
    else:
        return render(request, "shop/pages/accueil.html")


### Update Vetêment
def updateVet(request, id):
    vetementUpdate = Vetement.objects.get(id=id)
    formUpdateVet = PosteInsertVet(request.POST or None, instance=vetementUpdate)
    if formUpdateVet.is_valid():
        formUpdateVet.save()
        return redirect('administration:gestionProduit')

    if request.user.is_superuser:
        return render(request, "administration/pages/updateVet.html",
                      {'vetementUpdate': vetementUpdate, 'formUpdateVet': formUpdateVet})
    else:
        return render(request, "shop/pages/accueil.html")


### Update Produit Intérieur
def updateProInt(request, id):
    proIntUpdate = ProduitInterieur.objects.get(id=id)
    formUpdateProInt = PosteInsertProInt(request.POST or None, instance=proIntUpdate)
    if formUpdateProInt.is_valid():
        formUpdateProInt.save()
        return redirect('administration:gestionProduit')

    if request.user.is_superuser:
        return render(request, "administration/pages/updateProInt.html",
                      {'proIntUpdate': proIntUpdate, 'formUpdateProInt': formUpdateProInt})
    else:
        return render(request, "shop/pages/accueil.html")


### Update Produit Cosmétique
def updateProCos(request, id):
    proCosUpdate = Cosmetique.objects.get(id=id)
    formUpdateProCos = PosteInsertProCos(request.POST or None, instance=proCosUpdate)
    if formUpdateProCos.is_valid():
        formUpdateProCos.save()
        return redirect('administration:gestionProduit')

    if request.user.is_superuser:
        return render(request, "administration/pages/updateProCos.html",
                      {'proCosUpdate': proCosUpdate, 'formUpdateProCos': formUpdateProCos})
    else:
        return render(request, "shop/pages/accueil.html")


## Update Prix
def updatePrix(request, id):
    produit = Produit.objects.get(id=id)
    prixUpdate = Prix.objects.get(produit=produit.id)
    formUpdatePrix = PosteUpdatePrix(request.POST or None, instance=prixUpdate)
    if formUpdatePrix.is_valid():
        formUpdatePrix.save()
        return redirect('administration:gestionProduit')

    if request.user.is_superuser:
        return render(request, "administration/pages/updatePrix.html",
                      {'prixUpdate': prixUpdate, 'formUpdatePrix': formUpdatePrix})
    else:
        return render(request, "shop/pages/accueil.html")


### Update Produit Cosmétique
def updateAtelier(request, id):
    atelierUpdate = Atelier.objects.get(id=id)
    formUpdateAtelier = PosteInsertAtelier(request.POST or None, instance=atelierUpdate)
    if formUpdateAtelier.is_valid():
        formUpdateAtelier.save()
        return redirect('administration:gestionAtelier')

    if request.user.is_superuser:
        return render(request, "administration/pages/updateAtelier.html",
                      {'atelierUpdate': atelierUpdate, 'formUpdateAtelier': formUpdateAtelier})
    else:
        return render(request, "shop/pages/accueil.html")


### Update stock de Vetêment
def updateStockVet(request, id):
    stockVetementUpdate = Vetement.objects.get(id=id)
    formUpdateStockVet = PosteUpdateStockVet(request.POST or None, instance=stockVetementUpdate)
    if formUpdateStockVet.is_valid():
        formUpdateStockVet.save()
        return redirect('administration:gestionStock')

    if request.user.is_superuser:
        return render(request, "administration/pages/updateStockVet.html",
                      {'stockVetementUpdate': stockVetementUpdate, 'formUpdateStockVet': formUpdateStockVet})
    else:
        return render(request, "shop/pages/accueil.html")


### Update stock de Produit Intérieur
def updateStockProInt(request, id):
    stockProIntUpdate = ProduitInterieur.objects.get(id=id)
    formUpdateStockProInt = PosteUpdateStockProInt(request.POST or None, instance=stockProIntUpdate)
    if formUpdateStockProInt.is_valid():
        formUpdateStockProInt.save()
        return redirect('administration:gestionStock')

    if request.user.is_superuser:
        return render(request, "administration/pages/updateStockProInt.html",
                      {'stockProIntUpdate': stockProIntUpdate, 'formUpdateStockProInt': formUpdateStockProInt})
    else:
        return render(request, "shop/pages/accueil.html")


### Update stock de Produit Cosmétique
def updateStockProCos(request, id):
    stockProCosUpdate = Cosmetique.objects.get(id=id)
    formUpdateStockProCos = PosteUpdateStockProCos(request.POST or None, instance=stockProCosUpdate)
    if formUpdateStockProCos.is_valid():
        formUpdateStockProCos.save()
        return redirect('administration:gestionStock')

    if request.user.is_superuser:
        return render(request, "administration/pages/updateStockProCos.html",
                      {'stockProCosUpdate': stockProCosUpdate, 'formUpdateStockProCos': formUpdateStockProCos})
    else:
        return render(request, "shop/pages/accueil.html")


## Formation client
def formationClient(request, id):
    clientFormation = Client.objects.get(id=id)
    formDesactiverClient = PosteDesativerClient(request.POST or None, instance=clientFormation)
    if formDesactiverClient.is_valid():
        formDesactiverClient.save()
        return redirect('administration:gestionClient')

    if request.user.is_superuser:
        return render(request, "administration/pages/formationClient.html",
                      {'clientFormation': clientFormation, 'formDesactiverClient': formDesactiverClient})
    else:
        return render(request, "shop/pages/accueil.html")


####### Bar de Recherche Client
def searchClient(request):
    if request.user.is_superuser:
        if request.method == "POST":
            searched = request.POST['searched']
            clients = Client.objects.filter(nom__contains=searched)
            return render(request, "administration/pages/searchClient.html", {'searched': searched, 'clients': clients})
        else:
            return render(request, "administration/pages/searchClient.html")
    else:
        return render(request, "shop/pages/accueil.html")


# ####### Bar de Recherche Commande
# def searchCommande(request):
#     if request.user.is_superuser:
#         if request.method == "POST":
#             searchedCommande = request.POST['searchedCommande']
#             commandes = Commande.objects.filter(comDatePaiement=searchedCommande)
#             return render(request, "administration/pages/searchCommande.html",
#                           {'searchedCommande': searchedCommande, 'commandes': commandes})
#         else:
#             return render(request, "administration/pages/searchCommande.html")
#     else:
#         return render(request, "shop/pages/accueil.html")
