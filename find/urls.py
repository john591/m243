from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets
from professionnel import views

urlpatterns = [
    path('', include('professionnel.urls')),
    path('admin/', admin.site.urls),
    #path('professionels/', views.UserProfilList.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
