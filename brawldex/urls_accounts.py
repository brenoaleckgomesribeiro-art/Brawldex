from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup_view, perfil_view


urlpatterns = [

    path(
        'signup/',
        signup_view,
        name='signup'
    ),

    path(
        'perfil/',
        perfil_view,
        name='perfil'
    ),

    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='password_change_form.html',
            success_url='/accounts/password_change/done/',
        ),
        name='password_change_custom',
    ),

    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='password_change_done.html',
        ),
        name='password_change_done_custom',
    ),

]