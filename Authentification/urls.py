from django.urls import path
from .views import *

urlpatterns = [
    path('connexion/', login_Page, name='login'),
    path('deconnexion/', logout_user, name='log-out'),
    path('inscription/<int:id>/', inscription_page, name='inscription'),
    path('upload/Photo_Profil', upload_profile_photo, name='upload-photo'),
    path('parametre/', parametre_compte, name='parametre'),
    path('delete/<str:type>/<int:id>/', supprimer_compte, name='supprimer-compte'),
    path('update/profile', update_profile, name='update-profile'),
    path('update/password', update_password, name='update-password'),
]
