# Generated by Django 3.0.5 on 2020-09-13 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionnel', '0002_auto_20200913_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofil',
            name='profession',
            field=models.CharField(choices=[('1', 'Webmaster'), ('2', 'Technicien help desk'), ('3', 'Graphiste'), ('4', 'Developpeur web'), ('5', 'Medecin'), ('6', 'Avocat'), ('7', 'Journaliste'), ('8', 'Chantre'), ('9', 'Artiste musicien'), ('10', 'Consultant en audit informatique')], max_length=200),
        ),
        migrations.DeleteModel(
            name='Profession',
        ),
    ]
