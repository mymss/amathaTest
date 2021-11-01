import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from accounts.models import Client
from shop.forms import PosteInsertVet, PosteInsertProInt, PosteInsertProCos, PosteInsertAtelier, PosteUpdateStockProCos, \
    PosteUpdateStockProInt, PosteUpdateStockVet, PosteUpdatePrix, PosteDesativerClient, PosteInsertPrix, \
    PosteUpdateStatutCommande
from shop.models import Vetement, Produit, Cosmetique, ProduitInterieur, Prix, Atelier, Commande, \
    LigneProduitCommande, LigneAtelierCommande


# Create your views here.

###############################################
## View Accueil Admin Test
###############################################
def accueilAdmin(request):
    context = {}
    # vérification si c'est l'admin ou non
    if request.user.is_superuser:
        # si oui
        return render(request, "administration/pages/accueilAdmin.html", context)
    # si non
    else:
        return render(request, "shop/pages/accueil.html", context)


###############################################
## View Gestion de Stock Test
###############################################
def gestionStock(request):
    # déclaration et initialisation des variables
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
    # déclaration et initialisation des variables
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
    # déclaration et initialisation des variables
    atelier = Atelier.objects.all()

    if request.user.is_superuser:
        return render(request, "administration/pages/gestionAtelier.html", {'atelier': atelier})
    else:
        return render(request, "shop/pages/accueil.html")


###############################################
## View Gestion de prix Test
###############################################
def gestionPrix(request):
    # déclaration et initialisation des variables
    prix = Prix.objects.all()
    produit = Produit.objects.all()

    if request.user.is_superuser:
        return render(request, "administration/pages/gestionPrix.html",
                      {'prix': prix, 'produit': produit})
    else:
        return render(request, "shop/pages/accueil.html")


###############################################
## View Gestion de client Test
###############################################
def gestionClient(request):
    # déclaration et initialisation des variables
    client = Client.objects.all()

    if request.user.is_superuser:
        return render(request, "administration/pages/gestionClient.html", {'client': client})
    else:
        return render(request, "shop/pages/accueil.html")


###############################################
## View Gestion de client Test
###############################################
def gestionCommande(request):
    # déclaration et initialisation des variables
    commandes = Commande.objects.all().order_by('comDate').reverse()
    totalProduit = 0
    totalAtelier = 0
    listeProduit = []
    listeAtelier = []
    totalCommande = []

    # calculer le total de chaque commande
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

    # mettre tout les variables dans le context pour les appeler après
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
    # déclaration et initialisation des variables
    detailsVet = Vetement.objects.get(id=id)

    if request.user.is_superuser:
        return render(request, "administration/pages/adminVetDetails.html", {'detailsVet': detailsVet})
    else:
        return render(request, "shop/pages/accueil.html")


### Détails ProInt Admin
def adminProIntDetails(request, id):
    # déclaration et initialisation des variables
    detailsProInt = ProduitInterieur.objects.get(id=id)

    if request.user.is_superuser:
        return render(request, "administration/pages/adminProIntDetails.html", {'detailsProInt': detailsProInt})
    else:
        return render(request, "shop/pages/accueil.html")


### Détails ProCos Admin
def adminProCosDetails(request, id):
    # déclaration et initialisation des variables
    detailsProCos = Cosmetique.objects.get(id=id)

    if request.user.is_superuser:
        return render(request, "administration/pages/adminProCosDetails.html", {'detailsProCos': detailsProCos})
    else:
        return render(request, "shop/pages/accueil.html")


### Détails Atelier Admin
def adminAtelierDetails(request, id):
    # déclaration et initialisation des variables
    detailsAtelier = Atelier.objects.get(id=id)

    if request.user.is_superuser:
        return render(request, "administration/pages/adminAtelierDetails.html", {'detailsAtelier': detailsAtelier})
    else:
        return render(request, "shop/pages/accueil.html")


### Détails client Admin
def adminClientDetails(request, id):
    # déclaration et initialisation des variables
    detailsClient = Client.objects.get(id=id)
    commandes = Commande.objects.filter(clientId=id).order_by('comDate').reverse()
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
    # déclaration et initialisation des variables
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
    # récupérer les formulaires dans forms.py
    if request.method == "POST":
        formInsertVet = PosteInsertVet(request.POST, request.FILES)

        if formInsertVet.is_valid():
            formInsertVet = formInsertVet.save(commit=False)
            formInsertVet.author = request.user
            formInsertVet.save()

            return redirect('administration:insertionPrix')

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
    # récupérer les formulaires dans forms.py
    if request.method == "POST":
        formInsertProInt = PosteInsertProInt(request.POST)

        if formInsertProInt.is_valid():
            formInsertProInt = formInsertProInt.save(commit=False)
            formInsertProInt.author = request.user
            formInsertProInt.save()

            return redirect('administration:insertionPrix')

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
    # récupérer les formulaires dans forms.py
    if request.method == "POST":
        formInsertProCos = PosteInsertProCos(request.POST)

        if formInsertProCos.is_valid():
            formInsertProCos = formInsertProCos.save(commit=False)
            formInsertProCos.author = request.user
            formInsertProCos.save()

            return redirect('administration:insertionPrix')

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
    # récupérer les formulaires dans forms.py
    if request.method == "POST":
        formInsertAtelier = PosteInsertAtelier(request.POST)
        date = request.POST['dateDebut']

        if date == str(datetime.datetime.today()) or date < str(datetime.datetime.today()):
            messages.error(request, "La date doit être supérieure à aujourd'hui")
        else:
            if formInsertAtelier.is_valid():
                # dateDebut = formInsertAtelier.cleaned_data['dateDebut']
                formInsertAtelier = formInsertAtelier.save(commit=False)
                formInsertAtelier.author = request.user
                formInsertAtelier.save()
                messages.success(request, 'Le nouvel atelier a bien été ajouté ')

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
    # déclaration et initialisation des variables
    vetementUpdate = Vetement.objects.get(id=id)
    formUpdateVet = PosteInsertVet(request.POST or None, instance=vetementUpdate)
    # valider la formulaire après la modification
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
    # déclaration et initialisation des variables
    proIntUpdate = ProduitInterieur.objects.get(id=id)
    formUpdateProInt = PosteInsertProInt(request.POST or None, instance=proIntUpdate)
    # valider la formulaire après la modification
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
    # déclaration et initialisation des variables
    proCosUpdate = Cosmetique.objects.get(id=id)
    formUpdateProCos = PosteInsertProCos(request.POST or None, instance=proCosUpdate)
    # valider la formulaire après la modification
    if formUpdateProCos.is_valid():
        formUpdateProCos.save()
        return redirect('administration:gestionProduit')

    if request.user.is_superuser:
        return render(request, "administration/pages/updateProCos.html",
                      {'proCosUpdate': proCosUpdate, 'formUpdateProCos': formUpdateProCos})
    else:
        return render(request, "shop/pages/accueil.html")


## Insertion Prix
def insertionPrix(request):
    ##Récupérer la dernière id
    # lastPro = Produit.objects.last().id
    # récupérer les formulaires dans forms.py
    if request.method == "POST":
        formInsertPrix = PosteInsertPrix(request.POST)

        if formInsertPrix.is_valid():
            formInsertPrix = formInsertPrix.save(commit=False)
            formInsertPrix.author = request.user
            formInsertPrix.save()

            return redirect('administration:gestionProduit')

    else:
        formInsertPrix = PosteInsertPrix()

    if request.user.is_superuser:
        return render(request, "administration/pages/insertionPrix.html",
                      {'formInsertPrix': formInsertPrix})
    else:
        return render(request, "shop/pages/accueil.html")


## Update Prix
def updatePrix(request, id):
    # déclaration et initialisation des variables
    prixUpdate = Prix.objects.get(produit=id)
    formUpdatePrix = PosteUpdatePrix(request.POST or None, instance=prixUpdate)
    # valider la formulaire après la modification
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
    # déclaration et initialisation des variables
    atelierUpdate = Atelier.objects.get(id=id)
    formUpdateAtelier = PosteInsertAtelier(request.POST or None, instance=atelierUpdate)
    # valider la formulaire après la modification
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
    # déclaration et initialisation des variables
    stockVetementUpdate = Vetement.objects.get(id=id)
    formUpdateStockVet = PosteUpdateStockVet(request.POST or None, instance=stockVetementUpdate)
    # valider la formulaire après la modification
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
    # déclaration et initialisation des variables
    stockProIntUpdate = ProduitInterieur.objects.get(id=id)
    formUpdateStockProInt = PosteUpdateStockProInt(request.POST or None, instance=stockProIntUpdate)
    # valider la formulaire après la modification
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
    # déclaration et initialisation des variables
    stockProCosUpdate = Cosmetique.objects.get(id=id)
    formUpdateStockProCos = PosteUpdateStockProCos(request.POST or None, instance=stockProCosUpdate)
    # valider la formulaire après la modification
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
    # déclaration et initialisation des variables
    clientFormation = Client.objects.get(id=id)
    formDesactiverClient = PosteDesativerClient(request.POST or None, instance=clientFormation)
    # valider la formulaire après la modification
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


####### Bar de Recherche Vetêment
def searchVet(request):
    # Vérifier si c'est ladmin ou non'
    if request.user.is_superuser:
        if request.method == "POST":
            # déclarer une variable qui prend la valeur écrite dans la bar de recherche
            searched = request.POST['searched']
            # il filtre les nom de vêtement par le mot écris dans la bar de recherche
            vetement = Vetement.objects.filter(nom__contains=searched)
            return render(request, "administration/pages/searchVet.html", {'searched': searched, 'vetement': vetement})
        else:
            return render(request, "administration/pages/searcVet.html")
    else:
        return render(request, "shop/pages/accueil.html")


####### Bar de Recherche Vetêment
def searchProCos(request):
    if request.user.is_superuser:
        if request.method == "POST":
            searched = request.POST['searched']
            cosmetique = Cosmetique.objects.filter(nom__contains=searched)
            return render(request, "administration/pages/searchProCos.html",
                          {'searched': searched, 'cosmetique': cosmetique})
        else:
            return render(request, "administration/pages/searchProCos.html")
    else:
        return render(request, "shop/pages/accueil.html")


####### Bar de Recherche Vetêment
def searchProInt(request):
    if request.user.is_superuser:
        if request.method == "POST":
            searched = request.POST['searched']
            proInterieur = ProduitInterieur.objects.filter(nom__contains=searched)
            return render(request, "administration/pages/searchProInt.html",
                          {'searched': searched, 'proInterieur': proInterieur})
        else:
            return render(request, "administration/pages/searchProInt.html")
    else:
        return render(request, "shop/pages/accueil.html")


####### Bar de Recherche Commande
def searchCommande(request):
    if request.user.is_superuser:
        if request.method == "POST":
            searched = request.POST['searched']
            commandes = Commande.objects.filter(comNumero__contains=searched)
            return render(request, "administration/pages/searchCommande.html",
                          {'searched': searched, 'commandes': commandes})
        else:
            return render(request, "administration/pages/searchCommande.html")
    else:
        return render(request, "shop/pages/accueil.html")


####### Bar de Recherche Atelier
def searchAtelier(request):
    if request.user.is_superuser:
        if request.method == "POST":
            searched = request.POST['searched']
            ateliers = Atelier.objects.filter(titre__contains=searched)
            return render(request, "administration/pages/searchAtelier.html",
                          {'searched': searched, 'ateliers': ateliers})
        else:
            return render(request, "administration/pages/searchAtelier.html")
    else:
        return render(request, "shop/pages/accueil.html")


####### Modifier statut commande
def updateStatutCommande(request, id):
    statutCommande = Commande.objects.get(id=id)
    formUpdateStatutCommande = PosteUpdateStatutCommande(request.POST or None, instance=statutCommande)
    if formUpdateStatutCommande.is_valid():
        formUpdateStatutCommande.save()
        return redirect('administration:gestionCommande')

    if request.user.is_superuser:
        return render(request, "administration/pages/updateStatutCommande.html",
                      {'statutCommande': statutCommande, 'formUpdateStatutCommande': formUpdateStatutCommande})
    else:
        return render(request, "shop/pages/accueil.html")
