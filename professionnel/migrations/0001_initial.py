# Generated by Django 3.0.5 on 2020-09-13 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commune', models.CharField(max_length=100)),
                ('quartier', models.CharField(max_length=100)),
                ('rue', models.CharField(max_length=150)),
                ('telephone', phone_field.models.PhoneField(blank=True, help_text='Numero de telephone: 0998540...', max_length=31)),
                ('libelle_profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professionnel.Profession')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
