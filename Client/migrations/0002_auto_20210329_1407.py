# Generated by Django 3.1.7 on 2021-03-29 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='code_postal',
            field=models.DecimalField(decimal_places=0, default='', max_digits=5),
        ),
        migrations.AlterField(
            model_name='client',
            name='numero_de_rue',
            field=models.DecimalField(decimal_places=0, default='', max_digits=3),
        ),
    ]
