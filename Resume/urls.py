from django.urls import path
from .views import *

urlpatterns = [
    path('profil/', mon_profil, name='mon-profil'),
    path('personnels/', tout_personnel, name='tout-personnel'),
    path('personnel/ajout/', Ajout_personnel, name='ajout-personnel'),
    path('personnel/<int:id>/modifier/', Ajout_personnel, name='modif-personnel'),
    path('competence/ajout/', Ajout_competence, name='ajout-competence'),
    path('competence/<int:id>/modifier/', Ajout_competence, name='modif-competence'),
    path('services/ajout/', Ajout_service, name='ajout-service'),
    path('services/<int:id>/modifier/', Ajout_service, name='modif-service'),
    path('realisations/ajout/', Ajout_realisation, name='ajout-realisation'),
    path('realisations/<int:id>/modifier/', Ajout_realisation, name='modif-realisation'),
    path('experience_academique/ajout/', Ajout_exp_Academique, name='ajout-expAca'),
    path('experience_academique/<int:id>/modifier/', Ajout_exp_Academique, name='modif-expAca'),
    path('experience_professionnel/ajout/', Ajout_exp_Professionnel, name='ajout-expPro'),
    path('experience_professionnel/<int:id>/modifier/', Ajout_exp_Professionnel, name='modif-expPro'),
    
    path('galerie/ajout/', ajout_photo_galerie, name='ajout-photo-galerie'),
]