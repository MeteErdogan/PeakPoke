# Generated by Django 3.1.7 on 2021-04-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0005_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Categorie_socioPro',
            field=models.CharField(choices=[('Etudiant', 'Etudiant'), ('Cadre', 'Cadre'), ('Professeur', 'Professeur')], max_length=100),
        ),
    ]