# Generated by Django 4.2.3 on 2024-03-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0004_remove_galerie_perso_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='description_profil',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Description du profil'),
        ),
        migrations.AddField(
            model_name='personnel',
            name='profil_actuel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Profil actuel'),
        ),
    ]
