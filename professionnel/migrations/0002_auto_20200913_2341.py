# Generated by Django 3.0.5 on 2020-09-13 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professionnel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofil',
            old_name='libelle_profession',
            new_name='profession',
        ),
    ]
