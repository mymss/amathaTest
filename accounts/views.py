from django.shortcuts import render, redirect
from .forms import ProfileForm, InfosUpdateForm, UserForm, EmailUpdateForm
from django.contrib.auth.decorators import login_required
from shop.models import Produit, Photo

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
def favourite_list(request):
    produit = Produit.objects.all()
    new = produit.filter(favoris=request.user.pk)
    listePhoto = []

    for pro in new:
        photos = Photo.objects.all().get(produitId_id=pro.id)
        listePhoto.append(photos)

    fav_number = new.count()
    bool = False

    if fav_number <= 0:
        bool = True

    context = {
        'new': new,
        'bool': bool,
        'fav_number': fav_number,
        'listePhoto': listePhoto,
    }
    return render(request, 'accounts/pages/favs.html', context)

# Create your views here.

# Register

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            return redirect('account:login')

    else:
        form = UserForm()
        profile_form = ProfileForm()


    context = {
     'form': form,
     'profile': profile_form,
    }

    return render(request, 'accounts/pages/register.html', context)

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

    if request.method =='POST':
        form = InfosUpdateForm(request.POST, instance=request.user.client)
        if form.is_valid():
            form.save()
            return redirect('account:informations')
    else :
        form = InfosUpdateForm(request.POST, instance=request.user.client)
    context={
        'form': form,
    }
    return render(request, 'accounts/pages/update_infosClient.html',context)

# /* Update email */
@login_required
def UpdateEmail(request):
    if request.method =='POST':
        form = EmailUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:informations')
    else :
        form = EmailUpdateForm(request.POST, instance=request.user)
    context={
        'form': form,
    }
    return render(request, 'accounts/pages/update_email.html', context)