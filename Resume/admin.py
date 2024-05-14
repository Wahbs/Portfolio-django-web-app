from django.contrib import admin
from Resume.models import *

# Register your models here.

class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'sexe' )

admin.site.register(Personnel, PersonnelAdmin)

class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('personnel', 'competence', )

admin.site.register(Competences, CompetenceAdmin)

class ExperienceAca(admin.ModelAdmin):
    list_display = ('personnel', 'ecole', 'filiere' )

admin.site.register(Experience_Academique, ExperienceAca)

class ExperiencePro(admin.ModelAdmin):
    list_display = ('personnel', 'entreprise', 'poste' )

admin.site.register(Experience_Professionnelle, ExperiencePro)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('personnel', 'service', 'description' )

admin.site.register(Services_proposes, ServiceAdmin)

class RealisationAdmin(admin.ModelAdmin):
    list_display = ('personnel', 'realisation' )

admin.site.register(Realisation, RealisationAdmin)

class ImageReaAdmin(admin.ModelAdmin):
    list_display = ('realisation', 'photo' )

admin.site.register(Image_realisation, ImageReaAdmin)

class GalerieAdmin(admin.ModelAdmin):
    list_display = ('personnel', 'photo', )

admin.site.register(Galerie_perso, GalerieAdmin)

class ReglageAdmin(admin.ModelAdmin):
    list_display = ('personnel', 'poste_actuel' )

admin.site.register(Reglage, ReglageAdmin)
