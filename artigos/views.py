from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Artigo
from .forms import RegistoForm, ArtigoForm, ComentarioForm
# Create your views here.

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)

        if form.is_valid():
            user = form.save()

            grupo = Group.objects.get(name='autores')
            user.groups.add(grupo)

            login(request, user)

            return redirect('lista_artigos')

    else:
        form = RegistoForm()

    return render(request, 'artigos/registo.html', {'form': form})

def criar_artigo_view(request):


    if not request.user.groups.filter(name='autores').exists():
        return redirect('lista_artigos')

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)

        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()

            return redirect('lista_artigos')

    else:
        form = ArtigoForm()

    return render(request, 'artigos/criar_artigo.html', {'form': form})


@login_required
def editar_artigo_view(request, id):

    if not request.user.groups.filter(name='autores').exists():
        return redirect('lista_artigos')

    artigo = get_object_or_404(Artigo,id=id,autor=request.user)

    if request.method == 'POST':
        form = ArtigoForm(request.POST,request.FILES,instance=artigo)

        if form.is_valid():
            form.save()
            return redirect('detalhe_artigo', id=id)

    else:
        form = ArtigoForm(instance=artigo)

    return render(request, 'artigos/editar_artigo.html', {'form': form})


def lista_artigos_view(request):

    artigos = Artigo.objects.all().order_by('-data_criacao')
    context={'artigos': artigos}

    return render(request, 'artigos/lista_artigos.html', context)

def detalhe_artigo_view(request, id):

    artigo = get_object_or_404(Artigo, id=id)

    comentarios = artigo.comentarios.all()

    if request.method == 'POST':

        if request.user.is_authenticated:

            form = ComentarioForm(request.POST)

            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.autor = request.user
                comentario.artigo = artigo
                comentario.save()

                return redirect('detalhe_artigo', id=id)

    else:
        form = ComentarioForm()
    context={'artigo': artigo,'comentarios': comentarios,'form': form}
    return render(request, 'artigos/detalhe_artigo.html', context)


@login_required
def like_artigo(request, id):

    artigo = get_object_or_404(Artigo, id=id)

    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)

    return redirect('detalhe_artigo', id=id)