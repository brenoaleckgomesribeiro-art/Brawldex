from django.urls import path

from .views import (
    home_view,
    sobre_view,
    brawlers_view,
    brawler_detail,
    brawler_create,
    brawler_update,
    brawler_delete
)


urlpatterns = [

    path(
        '',
        home_view,
        name='home'
    ),

    path(
        'sobre/',
        sobre_view,
        name='sobre'
    ),

    path(
        'brawlers/',
        brawlers_view,
        name='brawlers'
    ),

    path(
        'brawlers/<int:id>/',
        brawler_detail,
        name='brawler_detail'
    ),

    path(
        'brawlers/criar/',
        brawler_create,
        name='brawler_create'
    ),

    path(
        'brawlers/<int:id>/editar/',
        brawler_update,
        name='brawler_update'
    ),

    path(
        'brawlers/<int:id>/excluir/',
        brawler_delete,
        name='brawler_delete'
    ),

]