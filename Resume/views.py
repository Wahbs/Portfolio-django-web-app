from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from Authentification.models import User
# Create your views here.

def index_page(request):

    context = {
        'type': 'index',
    }
    return render(request, 'index.html', context)

def tout_personnel(request):
    if request.user.privilege == 0:
        list_personnels = Personnel.objects.all()
        personnel = None
        if request.method == 'GET': 
            if 'req' in request.GET:
                personnel = get_object_or_404(Personnel, id=request.GET['req'])
                if personnel:
                    request.session['idpersonnel'] = personnel.id

        context = {
            'list_personnels': list_personnels, 'personnel': personnel,
            'type': 'dashbord',
        }
        return render(request, 'Resume/tout_personnel.html', context)

def Ajout_personnel(request, id=None):
    page = 'Informations personnelles'
    if id is None:
        form =PersonnelForm()
    else:
        page = 'Modifier mes informations'
        if request.user.privilege == 0 or request.user.personnel.id == id:
            personnel = get_object_or_404(Personnel, id=id)
            form = PersonnelForm(instance=personnel)
    
    if request.method == 'POST':
        if id:
            form = PersonnelForm(request.POST, instance=personnel)
        else:
            form = PersonnelForm(request.POST)
        
        if form.is_valid():
            personnel = form.save(commit=False)
            personnel.save()

            return redirect('inscription', personnel.id, )
    context = {
        'form': form, 'type': 'rien', 'page': page,
    }   
    return render(request, 'Resume/formulaire.html', context)

def Ajout_competence(request, id=None):
    page = 'Ajouter une compétence'
    personnel = None
    if 'idpersonnel' in request.session:
        personnel = get_object_or_404(Personnel, id=request.session['idpersonnel'])
    if id is None:
        form = CompetenceForm()
    else:
        page = 'Modifier une compétence'
        if request.user.privilege == 0 or request.user.personnel == personnel:
            competence = get_object_or_404(Competences, id=id)
            form = CompetenceForm(instance=competence)
    
    if request.method == 'POST':
        if id:
            form = CompetenceForm(request.POST, instance=competence)
        else:
            form = CompetenceForm(request.POST)
        
        if form.is_valid():
            competence = form.save(commit=False)
            competence.personnel = personnel
            competence.save()

            return redirect('accueil-APPLI')
    context = {
        'form': form, 'type': 'dashbord', 'page': page,
    }   
    return render(request, 'Resume/formulaire.html', context)

def Ajout_service(request, id=None):
    page = 'Proposer un service'
    personnel = None
    if 'idpersonnel' in request.session:
        personnel = get_object_or_404(Personnel, id=request.session['idpersonnel'])
    if id is None:
        form = ServiceForm()
    else:
        page = 'Modifier service proposé'
        if request.user.privilege == 0 or request.user.personnel == personnel:
            service = get_object_or_404(Services_proposes, id=id)
            form = ServiceForm(instance=service)
    
    if request.method == 'POST':
        if id:
            form = ServiceForm(request.POST, request.FILES,instance=service)
        else:
            form = ServiceForm(request.POST, request.FILES)
        
        if form.is_valid():
            service = form.save(commit=False)
            service.personnel = personnel
            service.save()

            return redirect('accueil-APPLI')
    context = {
        'form': form, 'type': 'dashbord', 'page': page,
    }   
    return render(request, 'Resume/formulaire.html', context)

def Ajout_realisation(request, id=None):
    page = 'Enregistrer une réalisation'
    personnel = None
    if 'idpersonnel' in request.session:
        personnel = get_object_or_404(Personnel, id=request.session['idpersonnel'])
    if id is None:
        form = RealisationForm()
    else:
        page = 'Modifier la réalisation'
        if request.user.privilege == 0 or request.user.personnel == personnel:
            realisation = get_object_or_404(Realisation, id=id)
            form = RealisationForm(instance=realisation)
    
    if request.method == 'POST':
        if id:
            form = RealisationForm(request.POST, instance=realisation)
        else:
            form = RealisationForm(request.POST)
        
        if form.is_valid():
            realisation = form.save(commit=False)
            realisation.personnel = personnel
            realisation.save()

            return redirect('accueil-APPLI')
    context = {
        'form': form, 'type': 'dashbord', 'page': page,
    }   
    return render(request, 'Resume/formulaire.html', context)

def Ajout_exp_Academique(request, id=None):
    page = 'Enregistrer une expérience académique'
    personnel = None
    if 'idpersonnel' in request.session:
        personnel = get_object_or_404(Personnel, id=request.session['idpersonnel'])
    if id is None:
        form = ExpAcademiqueForm()
    else:
        page = 'Modifier l\'expérience'
        if request.user.privilege == 0 or request.user.personnel == personnel:
            experience = get_object_or_404(Experience_Academique, id=id)
            form = ExpAcademiqueForm(instance=experience)
    
    if request.method == 'POST':
        if 'idpersonnel' in request.session:
            personnel = get_object_or_404(Personnel, id=request.session['idpersonnel'])
        if id:
            form = ExpAcademiqueForm(request.POST, instance=experience)
        else:
            form = ExpAcademiqueForm(request.POST)
        
        if form.is_valid():
            experience = form.save(commit=False)
            experience.personnel = personnel
            experience.save()

            return redirect('accueil-APPLI')
    context = {
        'form': form, 'type': 'dashbord', 'page': page,
    }   
    return render(request, 'Resume/formulaire.html', context)

def Ajout_exp_Professionnel(request, id=None):
    page = 'Enregistrer une expérience professionnelle'
    personnel = None
    if 'idpersonnel' in request.session:
        personnel = get_object_or_404(Personnel, id=request.session['idpersonnel'])
    if id is None:
        form = ExpProfessionnelForm()
    else:
        page = 'Modifier l\'expérience professionnelle '
        if request.user.privilege == 0 or request.user.personnel.id == id:
            experience = get_object_or_404(Experience_Professionnelle, id=id)
            form = ExpProfessionnelForm(instance=experience)
    
    if request.method == 'POST':
        if id:
            form = ExpProfessionnelForm(request.POST, instance=experience)
        else:
            form = ExpProfessionnelForm(request.POST)
        
        if form.is_valid():
            experience = form.save(commit=False)
            experience.personnel = personnel
            experience.save()

            return redirect('accueil-APPLI')
    context = {
        'form': form, 'type': 'dashbord', 'page': page,
    }   
    return render(request, 'Resume/formulaire.html', context)

def accueil(request):
    if request.user.is_authenticated:
        if request.user.privilege == 0:
            return redirect('accueil-APPLI')
        elif request.user.privilege > 0:
            return redirect('accueil-admin') 
    else:
        return redirect('index')

def accueil_visiteur(request, personnel):
    user = User.objects.filter(username=personnel)
    if user:
        personnel = get_object_or_404(Personnel, id=user[0].personnel.id)
    else: 
        if 'idpersonnel' in request.session:
            personnel = get_object_or_404(Personnel, id=request.session['idpersonnel'])
            print('ouiii')


    context = {
        'personnel': personnel, 'type': 'visiteur', 'banniere': False,
    }
    return render(request, 'Resume/accueil.html', context)

def ajout_photo_galerie(request, id=None):
    personnel = None
    if 'idpersonnel' in request.session:
        personnel = get_object_or_404(Personnel, id=request.session['idpersonnel'])
    form = GaleriePhotoForm()

    if request.method == 'POST':
        form = GaleriePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.personnel = personnel
            photo.save()
            if request.user.privilege == 0:
                return redirect('accueil-APPLI')
    context = {
        'type': 'dashbord', 'form': form,
    }
    return render(request, 'Resume/formulaire.html', context)

def mon_profil(request):

    personnel = None
    if 'idpersonnel' in request.session:
        personnel = get_object_or_404(Personnel, pk=request.session['idpersonnel'])
    if request.user.personnel == personnel:
        if request.method == 'GET':
            url = request.GET
        context = {
            'personnel':personnel, 'type':'manage', 'url':url,
        }
        return render(request, 'Resume/mon_profil.html', context)