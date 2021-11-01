import datetime

from django.core.mail import EmailMessage, message
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from amatha import settings
from .forms import ProfileForm, InfosUpdateForm, UserForm, EmailUpdateForm
from django.contrib.auth.decorators import login_required
from shop.models import Produit, Atelier
from django.contrib import messages
from django.views.generic import View
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator

@login_required
def favourite_add_cos(request, id):
    produit = Produit.objects.get(id=id)
    if produit.favoris.filter(id=request.user.pk).exists():
        produit.favoris.remove(request.user)

    else:
        produit.favoris.add(request.user)

    context = {
        'produit': produit,

    }
    return redirect('shop:cosmetique')


@login_required
def favourite_add_vet(request, id):
    produit = Produit.objects.get(id=id)
    if produit.favoris.filter(id=request.user.pk).exists():
        produit.favoris.remove(request.user)

    else:
        produit.favoris.add(request.user)

    context = {
        'produit': produit,

    }
    return redirect('shop:vetements')


@login_required
def favourite_add_proInt(request, id):
    produit = Produit.objects.get(id=id)
    if produit.favoris.filter(id=request.user.pk).exists():
        produit.favoris.remove(request.user)

    else:
        produit.favoris.add(request.user)

    context = {
        'produit': produit,

    }
    return redirect('shop:produitInterieur')


@login_required
def favourite_add_atelier(request, id):
    atelier = Atelier.objects.get(id=id)
    if atelier.favorisAtelier.filter(id=request.user.pk).exists():
        atelier.favorisAtelier.remove(request.user)

    else:
        atelier.favorisAtelier.add(request.user)

    context = {
        'atelier': atelier,

    }
    return redirect('shop:atelier')


@login_required
def favourite_list(request):
    produit = Produit.objects.all()
    atelier = Atelier.objects.all()
    new = produit.filter(favoris=request.user.pk)
    newate = atelier.filter(favorisAtelier=request.user.pk)
    # listePhoto = []
    #
    # for pro in new:
    #     photos = Photo.objects.all().get(produitId_id=pro.id)
    #     listePhoto.append(photos)

    fav_number = new.count()
    fav_numberate = newate.count()
    bool = False

    if fav_number <= 0 and fav_numberate <= 0:
        bool = True

    context = {
        'new': new,
        'bool': bool,
        'fav_number': fav_number,
        'fav_numberate': fav_numberate,
        'newate': newate,
    }
    return render(request, 'accounts/pages/favs.html', context)


# Create your views here.

# Register


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        username = request.POST['username']
        mail = request.POST.get('email')
        ddn = request.POST.get('dateNaissance')

        if User.objects.filter(email=mail).exclude(username=username).exists():
            messages.error(request, 'Ce mail est déjà existant !')
        elif ddn > str(datetime.date.today()):
            messages.error(request, 'Date de naissance impossible !')
        else:
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active= False
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                messages.success(request, "Pour confirmer votre inscription, nous vous avons envoyé un mail de confirmation d'inscription.")
                # getting domain we are on
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                link = reverse('account:activate', kwargs={'uidb64':uidb64,'token':token_generator.make_token(user),})
                activate_url = 'http://'+domain+link

                email_body = 'Bienvenue '+user.username+' ,pour vérifier ton adresse mail et finaliser ton inscription cliques sur ce lien\n'+ activate_url
                email_subject = 'Activation du compte'

                email = EmailMessage(email_subject, email_body,settings.EMAIL_HOST_USER,[mail])
                email.send(fail_silently=False)
                messages.success(request, 'Le compte a bien été créé')
                return redirect('account:login')
    else:
        form = UserForm()
        profile_form = ProfileForm()

    context = {
        'form': form,
        'profile': profile_form,
    }

    return render(request, 'accounts/pages/register.html', context)


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user,token):
                return redirect('account:login'+ "?message=" + "Utilisateur déjà authentifié")

            if user.is_active:
                return redirect('shop:accueil')
            user.is_active =True
            user.save()

            messages.success(request,'Votre compte a été activé avec succès.')

            return redirect('shop:accueil')

        except Exception as ex:
            pass
        return redirect('account:login')

# Infos client
@login_required
def informations(request):
    infos = request.user.client
    context = {
        'infos': infos,
    }
    return render(request, 'accounts/pages/infosClient.html', context)


# /* Update infos personnelles */
@login_required
def UpdateInfos(request):
    if request.method == 'POST':
        form = InfosUpdateForm(request.POST, instance=request.user.client)
        if form.is_valid():
            form.save()
            messages.success(request,'Tes informations ont bien étés modifiées !')
            return redirect('account:informations')
    else:
        form = InfosUpdateForm(request.POST, instance=request.user.client)
    context = {
        'form': form,
    }
    return render(request, 'accounts/pages/update_infosClient.html', context)


# /* Update email */
@login_required
def UpdateEmail(request):
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:informations')
    else:
        form = EmailUpdateForm(request.POST, instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/pages/update_email.html', context)


#################################################################################################
########## Bar de Recherche #############
@login_required
def favourite_add_produit_search(request, id):
    produit = Produit.objects.get(id=id)
    if produit.favoris.filter(id=request.user.pk).exists():
        produit.favoris.remove(request.user)

    else:
        produit.favoris.add(request.user)

    context = {
        'produit': produit,

    }
    return redirect('shop:accueil')