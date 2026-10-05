from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('brawldex.urls')
    ),

    # Rotas customizadas (signup, perfil, trocar senha)
    # Precisam vir ANTES do auth.urls, senão não sobrescrevem nada.
    path(
        'accounts/',
        include('brawldex.urls_accounts')
    ),

    # Rotas padrão do Django (login, logout, password reset, etc)
    path(
        'accounts/',
        include('django.contrib.auth.urls')
    ),

]


# Servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )