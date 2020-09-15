from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from . serializers import UserProfilSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm, UserProfilForm, UserSearchForm

def home(request):
    if request.user.is_authenticated:
        return redirect('accueil')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')
            else:
                messages.info(request, 'Nom utilisateur ou Mot de passe incorrect!')

        context = {}
        return render(request, "professionnel/index.html", context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('accueil')
    else:
        form = CreateUserForm()
        profil_form = UserProfilForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            profil_form = UserProfilForm(request.POST)

            if form.is_valid() and profil_form.is_valid():
                user = form.save()

                profil = profil_form.save(commit=False)
                profil.user = user

                profil.save()

                user = form.cleaned_data.get('username')
                messages.success(request, user + ' ' + 'votre compte a été créé !' )

                return redirect('home')

        context = {'form':form, 'profil_form':profil_form}
        return render(request, 'professionnel/register.html', context)

@login_required(login_url='home')
def accueilPage(request):

    context = {}
    return render(request, 'professionnel/accueil.html', context)

@login_required(login_url='home')
def findPage(request):
    queryset = UserProfil.objects.all()
    form = UserSearchForm(request.POST or None)

    context = {'queryset':queryset,'form':form}
    if request.method == 'POST':
        queryset = UserProfil.objects.all().order_by('id').filter(profession__icontains=form['profession'].value(),commune__icontains=form['commune'].value(),quartier__icontains=form['quartier'].value())
        context = {
            'queryset':queryset,
            'form':form
        }
    return render(request, 'professionnel/find.html', context)
"""
class UserProfilList(APIView):

    def get(self, request):
        userProfessional = UserProfil.objects.all()
        serializer = UserProfilSerializer(userProfessional, many= True)
        return Response(serializer.data)


    def post(self):
        pass
"""
