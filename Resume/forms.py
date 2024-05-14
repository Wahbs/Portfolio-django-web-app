from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *


class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        exclude = ('date_created',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'exemple@gmail.com'}),
            'motivations': forms.TextInput(attrs={'placeholder': 'Motivations personnelles', 'rows': 2}),
            'resume': forms.Textarea(attrs={'placeholder': 'Resumé', 'row':2}),
            'date_naissance': forms.DateInput(attrs={'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(PersonnelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
            if visible.name == 'sexe':
                visible.field.widget.attrs['class'] = 'form-select form-select-sm'
            if self.errors:
                if visible.errors:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-invalid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'
                else:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-valid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm'

    def clean(self):
        super(PersonnelForm, self).clean()
        # Recuperation des champs du formulaire
        #nom = self.cleaned_data.get('last_name')
        #prenom = self.cleaned_data.get('first_name')
        nom = self.cleaned_data.get('nom')
        email = self.cleaned_data.get('email')
        #date = self.cleaned_data.get('dateNaiss')
        dateNaiss = self.cleaned_data.get('date_naissance')
        # Gestion des erreurs
        if nom == None or str(nom).strip() == '':
            self.add_error('nom', 'Le nom du personnel est obligatoire')

        if email == None or str(email).strip() == '':
            self.add_error('email', 'L\'adresse mail est obligatoire')

        if dateNaiss == None or str(dateNaiss).strip() == '':
            self.add_error('date_naissance', 'La date de naissance est obligatoire')
        return self.cleaned_data


class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competences
        exclude = ('personnel', 'date_created',)

    def __init__(self, *args, **kwargs):
        super(CompetenceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
            if visible.name == 'sexe':
                visible.field.widget.attrs['class'] = 'form-select form-select-sm'
            if self.errors:
                if visible.errors:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-invalid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'
                else:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-valid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'

    def clean(self):
        super(CompetenceForm, self).clean()
        # Recuperation des champs du formulaire
        #nom = self.cleaned_data.get('last_name')
        #prenom = self.cleaned_data.get('first_name')
        competence = self.cleaned_data.get('competence')
        description = self.cleaned_data.get('description')
        #date = self.cleaned_data.get('dateNaiss')
        niveau = self.cleaned_data.get('niveau')
        # Gestion des erreurs
        if competence == None or str(competence).strip() == '':
            self.add_error('competence', 'La competence est obligatoire')

        if description == None or str(description).strip() == '':
            self.add_error('description', 'La description est obligatoire')

        if niveau == None or str(niveau).strip() == '':
            self.add_error('niveau', 'Le niveau de la competence est obligatoire')
        return self.cleaned_data

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services_proposes
        exclude = ('personnel', 'date_created',)

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
            if visible.name == 'sexe':
                visible.field.widget.attrs['class'] = 'form-select form-select-sm'
            if self.errors:
                if visible.errors:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-invalid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'
                else:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-valid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'

    def clean(self):
        super(ServiceForm, self).clean()
        # Recuperation des champs du formulaire
        #nom = self.cleaned_data.get('last_name')
        #prenom = self.cleaned_data.get('first_name')
        service = self.cleaned_data.get('service')
        description = self.cleaned_data.get('description')
        #date = self.cleaned_data.get('dateNaiss')
        photo = self.cleaned_data.get('photo')
        # Gestion des erreurs
        if service == None or str(service).strip() == '':
            self.add_error('service', 'Le service proposé est obligatoire')

        if description == None or str(description).strip() == '':
            self.add_error('description', 'La description du service proposé est obligatoire')

        if photo == None or str(photo).strip() == '':
            self.add_error('photo', 'Veuillez enregistrer une icone du service')
        return self.cleaned_data

class ExpAcademiqueForm(forms.ModelForm):
    class Meta:
        model = Experience_Academique
        exclude = ('personnel','date_created',)
        
    def __init__(self, *args, **kwargs):
        super(ExpAcademiqueForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
            if visible.name == 'sexe':
                visible.field.widget.attrs['class'] = 'form-select form-select-sm'
            if self.errors:
                if visible.errors:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-invalid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'
                else:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-valid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'

    def clean(self):
        super(ExpAcademiqueForm, self).clean()
        # Recuperation des champs du formulaire
        #nom = self.cleaned_data.get('last_name')
        #prenom = self.cleaned_data.get('first_name')
        ecole = self.cleaned_data.get('ecole')
        filiere = self.cleaned_data.get('filiere')
        #date = self.cleaned_data.get('dateNaiss')
        diplome = self.cleaned_data.get('diplome')
        # Gestion des erreurs
        if ecole == None or str(ecole).strip() == '':
            self.add_error('ecole', 'Le nom de l\'etablissement est obligatoire')

        if filiere == None or str(filiere).strip() == '':
            self.add_error('filiere', 'La filiere est obligatoire')

        if diplome == None or str(diplome).strip() == '':
            self.add_error('diplome', 'Veuillez enregistrer le diplome obtenu')
        return self.cleaned_data

class ExpProfessionnelForm(forms.ModelForm):
    class Meta:
        model = Experience_Professionnelle
        exclude = ('personnel', 'date_created',)
        widgets = {
            'date_debut': forms.DateInput(attrs={'type':'date'}),
            'date_fin': forms.DateInput(attrs={'type':'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(ExpProfessionnelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
            if visible.name == 'sexe':
                visible.field.widget.attrs['class'] = 'form-select form-select-sm'
            if self.errors:
                if visible.errors:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-invalid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'
                else:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-valid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'

    def clean(self):
        super(ExpProfessionnelForm, self).clean()
        # Recuperation des champs du formulaire
        #nom = self.cleaned_data.get('last_name')
        #prenom = self.cleaned_data.get('first_name')
        poste = self.cleaned_data.get('poste')
        entreprise = self.cleaned_data.get('entreprise')
        # Gestion des erreurs
        if poste == None or str(poste).strip() == '':
            self.add_error('poste', 'Le poste est obligatoire')

        if entreprise == None or str(entreprise).strip() == '':
            self.add_error('entreprise', 'Le nom de la structure est obligatoire')

        return self.cleaned_data

class RealisationForm(forms.ModelForm):
    class Meta:
        model = Personnel
        exclude = ('personnel','date_created',)

    def __init__(self, *args, **kwargs):
        super(RealisationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
            if visible.name == 'sexe':
                visible.field.widget.attrs['class'] = 'form-select form-select-sm'
            if self.errors:
                if visible.errors:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-invalid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'
                else:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-valid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'

    def clean(self):
        super(RealisationForm, self).clean()
        realisation = self.cleaned_data.get('realisation')
        description = self.cleaned_data.get('description')
        # Gestion des erreurs
        if realisation == None or str(realisation).strip() == '':
            self.add_error('realisation', 'L\'intitulé de la réalisation est obligatoire')

        if description == None or str(description).strip() == '':
            self.add_error('description', 'La description de la realisation est obligatoire')

        return self.cleaned_data

class ImageRealisationForm(forms.ModelForm):
    class Meta:
        model = Image_realisation
        exclude = ('date_created',)
        widgets = {
            'photo': forms.ImageField(),
        }


    def __init__(self, *args, **kwargs):
        super(ImageRealisationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
            if visible.name == 'sexe':
                visible.field.widget.attrs['class'] = 'form-select form-select-sm'
            if self.errors:
                if visible.errors:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-invalid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'
                else:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-valid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'

    def clean(self):
        super(ImageRealisationForm, self).clean()
        photo = self.cleaned_data.get('photo')
        # Gestion des erreurs
        if photo == None :
            self.add_error('photo', '')

        return self.cleaned_data

class GaleriePhotoForm(forms.ModelForm):
    class Meta:
        model = Galerie_perso
        fields = ('photo',)
        widgets = {
            'photo': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(GaleriePhotoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
            if visible.name == 'sexe':
                visible.field.widget.attrs['class'] = 'form-select form-select-sm'
            if self.errors:
                if visible.errors:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-invalid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'
                else:
                    visible.field.widget.attrs['class'] = 'form-control form-control-sm is-valid'
                    if visible.name == 'sexe':
                        visible.field.widget.attrs['class'] = 'form-select form-select-sm is-invalid'

    def clean(self):
        super(GaleriePhotoForm, self).clean()
        photo = self.cleaned_data.get('photo')
        if photo == None :
            self.add_error('photo', '')
        return self.cleaned_data
