from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from Resume.models import Personnel

# Create your models here.

class User(AbstractUser, PermissionsMixin):
    def __str__(self):
        return f'{self.personnel}'

    privilege_Choice = [
        (0, 0),
        (1, 1),
        (2, 2),
    ]
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=True, related_name='perscompte')
    email = models.EmailField(unique=False, blank=True, null=True)
    username = models.CharField(unique=True, max_length=30, verbose_name="Nom d'uilisateur", blank=True, null=True)
    photo_profil = models.ImageField(verbose_name='Photo de profil', upload_to='profils/', blank=True, null=True)
    privilege = models.SmallIntegerField(verbose_name='Priilège', choices=privilege_Choice, blank=True, default=3)
    date_created = models.DateField(verbose_name='Date creation compte', auto_now=True)
