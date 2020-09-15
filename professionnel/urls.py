from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("deconnexion/", views.logoutUser, name="logout"),
    path("creation_compte/", views.registerPage, name="creer"),
    path("accueil/", views.accueilPage, name="accueil"),
    path("trouver-un-professionnel/", views.findPage, name="find"),
]
