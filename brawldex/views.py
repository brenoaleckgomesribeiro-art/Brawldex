from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

from .models import Brawler
from .forms import BrawlerForm, CadastroForm, PerfilForm


# Ordem "oficial" das raridades (progressão do jogo)
ORDEM_RARIDADES = [
    'Comum',
    'Raro',
    'Super-raro',
    'Épico',
    'Mítico',
    'Lendário',
    'Ultralendário',
]


def home_view(request):

    total_brawlers = Brawler.objects.count()

    total_raridades = (
        Brawler.objects
        .values('raridade')
        .distinct()
        .count()
    )

    return render(request, 'home.html', {
        'total_brawlers': total_brawlers,
        'total_raridades': total_raridades,
    })


def sobre_view(request):
    return render(request, 'sobre.html')


def brawlers_view(request):

    raridades_no_banco = (
        Brawler.objects
        .values_list('raridade', flat=True)
        .distinct()
    )

    def chave_ordenacao(raridade):
        if raridade in ORDEM_RARIDADES:
            return (0, ORDEM_RARIDADES.index(raridade))
        return (1, raridade)

    raridades = sorted(raridades_no_banco, key=chave_ordenacao)

    raridade_selecionada = request.GET.get('raridade', '').strip()
    busca = request.GET.get('q', '').strip()

    brawlers = Brawler.objects.all()

    if raridade_selecionada:
        brawlers = brawlers.filter(raridade=raridade_selecionada)

    if busca:
        brawlers = brawlers.filter(nome__icontains=busca)

    return render(request, 'brawlers.html', {
        'brawlers': brawlers,
        'raridades': raridades,
        'raridade_selecionada': raridade_selecionada,
        'busca': busca,
    })


def brawler_detail(request, id):
    brawler = get_object_or_404(Brawler, id=id)

    return render(request, 'brawler_detail.html', {
        'brawler': brawler
    })


@login_required
def brawler_create(request):

    if request.method == 'POST':
        form = BrawlerForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('brawlers')

    else:
        form = BrawlerForm()

    return render(request, 'brawler_form.html', {
        'form': form
    })


@login_required
def brawler_update(request, id):

    brawler = get_object_or_404(Brawler, id=id)

    if request.method == 'POST':
        form = BrawlerForm(
            request.POST,
            request.FILES,
            instance=brawler
        )

        if form.is_valid():
            form.save()

            return redirect(
                'brawler_detail',
                id=brawler.id
            )

    else:
        form = BrawlerForm(instance=brawler)

    return render(request, 'brawler_form.html', {
        'form': form,
        'brawler': brawler
    })


@login_required
def brawler_delete(request, id):

    brawler = get_object_or_404(Brawler, id=id)

    if request.method == 'POST':
        brawler.delete()

        return redirect('brawlers')

    return render(request, 'brawler_confirm_delete.html', {
        'brawler': brawler
    })


# ============================================================
# CADASTRO E PERFIL
# ============================================================

def signup_view(request):
    """
    Cadastro público de usuário.
    Depois de criar, faz login automático e redireciona pra home.
    """

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                f'Bem-vindo ao BrawlDex, {user.username}!'
            )
            return redirect('home')

    else:
        form = CadastroForm()

    return render(request, 'signup.html', {
        'form': form
    })


@login_required
def perfil_view(request):
    """
    Ver e editar dados da conta: nome, sobrenome, email.
    Trocar senha fica em /accounts/password_change/ (view do Django).
    """

    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso.')
            return redirect('perfil')

    else:
        form = PerfilForm(instance=request.user)

    return render(request, 'perfil.html', {
        'form': form
    })