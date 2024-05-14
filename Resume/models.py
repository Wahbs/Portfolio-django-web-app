from django.db import models
from django.utils import timezone
# Create your models here.

class Personnel(models.Model):
    def __str__(self):
        return f'{self.nom}'
    
    sexe_choix = [
        ('Masculin', 'Masculin'),
        ('Feminin', 'Feminin'),
    ]
    nom = models.CharField(max_length=30, verbose_name='Nom', blank=True, null=True)
    prenom = models.CharField(max_length=30, verbose_name='Prenom', blank=True, null=True)
    sexe = models.CharField(max_length=10, verbose_name='Sexe', choices=sexe_choix, blank=True, null=True)
    date_naissance = models.DateField(verbose_name='Date de naissance', blank=True, null=True)
    telephone_1 = models.CharField(max_length=30, verbose_name='Telephone', blank=True, null=True)
    telephone_2 = models.CharField(max_length=30, verbose_name='Telephone', blank=True, null=True)
    email = models.EmailField(max_length=30, verbose_name='E-mail', blank=True, null=True)
    pays = models.CharField(max_length=30, verbose_name='Pays', blank=True, null=True)
    ville = models.CharField(max_length=30, verbose_name='ville', blank=True, null=True)
    resume = models.TextField(max_length=500, verbose_name='Resumé', blank=True, null=True)
    motivation = models.TextField(max_length=300, verbose_name='Motivations personnelles', blank=True, null=True)

    profil_actuel = models.CharField(max_length=100, verbose_name='Profil actuel', blank=True, null=True)
    description_profil = models.CharField(max_length=255, verbose_name='Description du profil', blank=True, null=True)

    date_created = models.DateField(verbose_name='Date creation', auto_now=True)

    def lien(self):
        if self.nom is not None and self.prenom is not None:
            return f'{self.nom}_{self.prenom}_{self.id}'
        elif self.nom is not None and self.prenom is None:
            return f'{self.nom}_{self.id}'
        
    def Age(self):
        today = timezone.now()
        age = today.year - self.date_naissance.year
        #age = diff.days // 365
        agestr = f'{age} ans'
        if age == 1:
            agestr = f'{age} an'
        if age<1:
            age = today.month - self.date_naissance.month
            agestr = f'{age} mois'
            if age < 1:
                age = today.day - self.date_naissance.day
                agestr = f'{age} jours'

        return agestr
    
class Competences(models.Model):
    def __str__(self):
        return f'{self.competence}'
    
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL, related_name='competencesperso', null=True, blank=True)
    competence = models.CharField(max_length=100, verbose_name='Competence', blank=True, null=True)
    description = models.CharField(max_length=200, verbose_name='Description de la compétence', blank=True, null=True)
    niveau = models.IntegerField(verbose_name='Niveau(%)', blank=True, null=True)
    date_created = models.DateField(verbose_name='date_created', blank=True, null=True, auto_now=True)   
    
class Services_proposes(models.Model):
    def __str__(self):
        return f'{self.competence}'
    
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL, related_name='serviceperso', null=True, blank=True)
    service = models.CharField(max_length=100, verbose_name='Services proposés', blank=True, null=True)
    description = models.CharField(max_length=200, verbose_name='Description du service', blank=True, null=True)
    photo = models.ImageField(verbose_name='Icone du service', upload_to='media/services/', blank=True, null=True)
    date_created = models.DateField(verbose_name='date_created', blank=True, null=True, auto_now=True)   

class Experience_Academique(models.Model):
    def __str__(self):
        return f'{self.ecole} {self.filiere}'
    
    statut_choix = [
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé'),
    ]
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL, related_name='ExpAcad', null=True, blank=True)
    annee_debut = models.IntegerField(verbose_name='Année debutée', blank=True, null=True)
    annee_fin = models.IntegerField(verbose_name='Année fini', blank=True, null=True)
    ecole = models.CharField(max_length=50, verbose_name='Etablissement', blank=True, null=True)
    filiere = models.CharField(max_length=50, verbose_name='Filière', blank=True, null=True)
    diplome = models.CharField(max_length=50, verbose_name='Diplome', blank=True, null=True)
    pays = models.CharField(max_length=50, verbose_name='Pays', blank=True, null=True)
    ville = models.CharField(max_length=50, verbose_name='Ville', blank=True, null=True)

    staut = models.CharField(max_length=30, verbose_name='Statut', choices=statut_choix,blank=True, null=True)
    date_created = models.DateField(verbose_name='date_created', blank=True, null=True, auto_now=True)

class Experience_Professionnelle(models.Model):
    def __str__(self):
        return f'{self.competence}'
    
    statut_choix = [
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé'),
    ]
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL, related_name='ExpPro', null=True, blank=True)
    date_debut = models.DateField(verbose_name='Date debut', blank=True, null=True)
    date_fin = models.DateField(verbose_name='Date fin', blank=True, null=True)
    entreprise = models.CharField(max_length=70, verbose_name='Nom de la structure', blank=True, null=True)
    poste = models.CharField(max_length=50, verbose_name='Poste', blank=True, null=True)
    description = models.CharField(max_length=150, verbose_name='Description du poste', blank=True, null=True)
    pays = models.CharField(max_length=50, verbose_name='Pays', blank=True, null=True)
    ville = models.CharField(max_length=50, verbose_name='Ville', blank=True, null=True)

    staut = models.CharField(max_length=30, verbose_name='Statut', choices=statut_choix,blank=True, null=True)
    date_created = models.DateField(verbose_name='date_created', blank=True, null=True, auto_now=True)

class Realisation(models.Model):
    def __str__(self):
        return f'{self.realisation}'
    
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL, related_name='realiseperso', null=True, blank=True)
    realisation = models.CharField(max_length=100, verbose_name='Lien du projet', blank=True, null=True)
    description = models.CharField(max_length=200, verbose_name='Description du projet', blank=True, null=True)
    date_created = models.DateField(verbose_name='date_created', blank=True, null=True, auto_now=True)   

class Image_realisation(models.Model):
    def __str__(self):
        return f'{self.realisation}'
    
    realisation = models.ForeignKey(Realisation, on_delete=models.SET_NULL, related_name='imgReali', null=True, blank=True)
    photo = models.ImageField(verbose_name='Image de la realisation', upload_to='realisations/', blank=True, null=True)
    date_created = models.DateField(verbose_name='date_created', blank=True, null=True, auto_now=True)   
    
class Galerie_perso(models.Model):
    def __str__(self):
        return f'{self.personnel}'
    
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL, related_name='GaleriPerso', null=True, blank=True)
    photo = models.ImageField(verbose_name='Image de la realisation', upload_to='galerie', blank=True, null=True)
    #description = models.CharField(max_length=200, verbose_name='Description de l\'image', blank=True, null=True)
    date_created = models.DateField(verbose_name='date_created', blank=True, null=True, auto_now=True)   
    
class Reglage(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL, related_name='ReglagePerso', null=True, blank=True)
    photo_profil = models.ForeignKey(Galerie_perso, on_delete=models.SET_NULL, related_name='profilperso', null=True, blank=True)
    photo_couverture = models.ForeignKey(Galerie_perso, on_delete=models.SET_NULL, related_name='couvertureperso', null=True, blank=True)
    poste_actuel = models.ForeignKey(Experience_Professionnelle, on_delete=models.SET_NULL, related_name='posteactuel', null=True, blank=True)
