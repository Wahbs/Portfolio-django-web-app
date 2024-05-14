from django.http import HttpResponseRedirect
from django.shortcuts import  render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
import pandas as pd
from django.utils import timezone
from . import forms
from django.db.models import Q
from Authentification.models import User
from Resume.models import *


# Create your views here.
def login_Page(request):
    form = forms.LoginForm()
    message = ''
    if request.user.is_authenticated:
        request.session['idpersonnel'] = request.user.personnel.id
        if request.user.privilege == 0:
            return redirect('accueil-admin')
        elif request.user.privilege >= 1:
            return redirect('accueil-temoin')
    
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                request.session['idpersonnel'] = request.user.personnel.id
                if user.privilege == 1:
                    return redirect('accueil-admin')
                if user.privilege >= 2:
                    return redirect('accueil-temoin')

            else:
                message = 'Identifiant invalide'
    context = {'form': form, 'type': 'rien', 'message': message     
    }
    return render(request, 'Authentification/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def inscription_page(request, id=None):
    form = forms.inscriptionForm()
    personnel = None
    if id:
        personnel = get_object_or_404(Personnel, id=id)
    if request.method == 'POST':
        if str(request.POST['username']).strip() == '' or request.POST['username']== None:
            if not form.is_valid():
                pass
            else:
                form = forms.inscriptionForm(request.POST)
        else:
            form = forms.inscriptionForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.personnel = personnel
                user.privilege = 1
                user.save()
                # login(request, user)
                #return redirect(settings.LOGIN_REDIRECT_URL)
                return redirect('login')
    else:
        form = forms.inscriptionForm()

    context = {'form': form, 'type': 'rien',           
    }
    return render(request, 'Authentification/inscription.html', context)

@login_required
def accueil_admin_Appli(request):
    if request.user.is_authenticated:
        if request.user.privilege == 0:
            if request.user.privilege == 0:
                list_personnels = Personnel.objects.all()
                personnel = None
                if request.method == 'GET': 
                    if 'req' in request.GET:
                        personnel = get_object_or_404(Personnel, id=request.GET['req'])
                        if personnel:
                            request.session['idpersonnel'] = personnel.id
                        realisation = Realisation.objects.filter(personnel=personnel)
                        service = Services_proposes.objects.filter(personnel=personnel)
                        competence = Competences.objects.filter(personnel=personnel)
                        exp_academique = Experience_Academique.objects.filter(personnel=personnel)
                        exp_professionnel = Experience_Professionnelle.objects.filter(personnel=personnel)
                        image_realisation = Image_realisation.objects.filter(realisation__in=realisation)
                        galerie = Galerie_perso.objects.filter(personnel=personnel)
                        reglage = Reglage.objects.filter(personnel=personnel)

                        context = { 'personnel': personnel, 'image_realisation': image_realisation, 'galerie': galerie,
                            'reglage': reglage, 'service': service, 'competence': competence, 'exp_professionnel': exp_professionnel,
                            'exp_academique': exp_academique, 'dashbord':1, 'list_personnels': list_personnels,
                        }
                        return render(request, 'Authentification/accueil_admin_appli.html', context=context)

            context = {
                'type': 'dashbord',
                'list_personnels': list_personnels, 'personnel': personnel,
            }
            return render(request, 'Authentification/accueil_admin_appli.html', context=context)
        elif request.user.privilege == 1:
            return redirect('accueil-admin')
    return redirect('login')
    
    #return render(request, 'inconnu.html')
    
@login_required
def accueil_admin(request):
    if request.user.is_authenticated:
        if request.user.privilege == 0:

            context = {

            }
            return render(request, 'Authentification/accueil_admin_appli.html', context=context)
        elif request.user.privilege == 1:
            personnel = None
            if 'idpersonnel' in request.session:
                personnel = get_object_or_404(Personnel, pk=request.session['idpersonnel'])
            context = {
                'personnel': personnel, 'banniere': False,
            }
            return render(request, 'Resume/accueil.html', context=context)
    return redirect('login')

def logout_user(request):
    logout(request)
    return redirect('login')


""" def inscription_page(request):
    form = forms.inscriptionForm()
    if request.method == 'POST':
        form = forms.inscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = forms.inscriptionForm()

    return render(request, 'Authentification/inscription.html', {'form': form})
 """

def upload_profile_photo(request):
    url = 'upload-photo'
    lien = 'Modifier les informations personnelles'
    if request.method == 'POST':
        form = forms.UploadProfilPhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.UploadProfilPhotoForm()
    return render(request, 'Authentification/update_profile.html', {'form': form, 'lien': lien, 'url': url})


def parametre_compte(request):
    if request.method == 'POST':
        pass
    context = {
        'type': 'dashbord',
    }
    return render(request, 'Authentification/ParametreCompte.html', context)


def update_profile(request):
    lien = 'Modifier photo'
    url = 'upload-profil'
    form = forms.inscriptionForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if 'update_pass' in request.POST:
            form = forms.UpdatePasswordForm(request.POST, instance=request.user)
        elif 'upload_photo' in request.POST :
            form = forms.UploadProfilPhotoForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            login(request, request.user)
            return redirect('home')
    else:
        form = forms.inscriptionForm(instance=request.user)

    return render(request, 'Authentification/update_profile.html', {'form': form, 'lien': lien, 'url': url })


def update_password(request):
    url = 'update-password'
    lien = 'Modifier les informations personnelles'
    form = forms.UpdatePasswordForm(request.POST, instance=request.user)
    if request.method == 'POST':
        form = forms.UpdatePasswordForm(request.POST, instance=request.user)
        log = request.user.username
        pwd = form.cleaned_data.get('password')
        connex = authenticate(username=log, password=pwd)
        if connex is not None:
            if form.is_valid():
                form.save()
                login(request, request.user)
                return redirect('home')
        else:
            form.fields['password'].widget.attrs['class'] = 'form-control is-invalid'
            form.add_error('password', 'Le mot de passe doit etre identique a l\'ancien')

    else:
        form = forms.UpdatePasswordForm(instance=request.user)

    return render(request, 'Authentification/update_profile.html', {'form': form, 'lien': lien, 'url': url })


def profil_personnel(request, id_vendeur):
    vendeur = get_object_or_404(User, id=id_vendeur)

    mois = timezone.date.strftime(vendeur.Date_created, "%B")
    match str(mois).lower():
        case "january":
            mois = "janvier"
        case "february":
            mois = "fevrier"
        case "march":
            mois = "mars"
        case "april":
            mois = "avril"
        case "may":
            mois = "mai"
        case "june":
            mois = "juin"
        case "july":
            mois = "juillet"
        case "august":
            mois = "aout"
        case "september":
            mois = "septembre"
        case "october":
            mois = "octobre"
        case "november":
            mois = "novembre"
        case "december":
            mois = "decembre"

    date_rejoint = timezone.date.strftime(vendeur.Date_created, "{} %Y".format(mois))
    context = {
        'vendeur': vendeur,
        'date_rejoint': date_rejoint,
    }
    return render(request, 'Authentification/profil_vendeur.html', context)

@login_required
def supprimer_compte(request, id=None):
    if id==None:
        exit()
    compte = get_object_or_404(User, id=id)
    compte.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
