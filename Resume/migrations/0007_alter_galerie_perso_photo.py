# Generated by Django 4.2.3 on 2024-03-27 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0006_alter_galerie_perso_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galerie_perso',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='galerie', verbose_name='Image de la realisation'),
        ),
    ]