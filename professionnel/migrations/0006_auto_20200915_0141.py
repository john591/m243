# Generated by Django 3.0.5 on 2020-09-14 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionnel', '0005_auto_20200914_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofil',
            name='commune',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofil',
            name='profession',
            field=models.CharField(blank=True, choices=[('Webmaster', 'Webmaster'), ('Technicien help desk', 'Technicien help desk'), ('Graphiste', 'Graphiste'), ('Developpeur web', 'Developpeur web'), ('Medecin', 'Medecin'), ('Avocat', 'Avocat'), ('Journaliste', 'Journaliste'), ('Chantre', 'Chantre'), ('cuisinier', 'cuisinier'), ('Architecte', 'Architecte'), ('gynecologue', 'gynecologue'), ('infirmier', 'infirmier'), ('Artiste musicien', 'Artiste musicien'), ('Consultant en audit informatique', 'Consultant en audit informatique')], max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofil',
            name='quartier',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
