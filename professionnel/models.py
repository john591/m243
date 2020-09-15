from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.

class UserProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choix_prof = (
        ('Webmaster','Webmaster'),
        ('Technicien help desk','Technicien help desk'),
        ('Graphiste','Graphiste'),
        ('Developpeur web','Developpeur web'),
        ('Medecin','Medecin'),
        ('Avocat','Avocat'),
        ('Journaliste','Journaliste'),
        ('Chantre','Chantre'),
        ('cuisinier','cuisinier'),
        ('Architecte','Architecte'),
        ('gynecologue','gynecologue'),
        ('infirmier','infirmier'),
        ('Artiste musicien','Artiste musicien'),
        ('Consultant en audit informatique','Consultant en audit informatique')
    )
    profession = models.CharField(max_length=200, choices=choix_prof)
    commune = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    rue = models.CharField(max_length=150)
    telephone = models.CharField(max_length=150, blank=True, help_text='Numero de telephone: 0998540...')

    def __str__(self):
        return f"{self.user.username} -> {self.profession}"
