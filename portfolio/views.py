from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home do projeto 🚀")

from django.shortcuts import render, get_object_or_404
from .models import *
from .forms   import *


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def licenciatura_view(request, id):
    licenciatura = Licenciatura.get(id=id) 
    return render(request, 'portfolio/licenciatura.html', {'licenciatura': licenciatura})

def docentes_view(request):
    docentes = Docente.objects.all()
    return render(request, 'portfolio/docentes.html', {'docentes': docentes})

def docente_view(request, id):
    docente = Docente.objects.get(id=id)  
    return render(request, 'portfolio/docente.html', {'docente': docente})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def uc_view(request, id):
    uc = UnidadeCurricular.objects.get(id=id)  
    return render(request, 'portfolio/uc.html', {'uc': uc})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def tecnologia_view(request, id):
    tecnologia = Tecnologia.objects.get(id=id)  
    return render(request, 'portfolio/tecnologia.html', {'tecnologia': tecnologia})

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def competencia_view(request, id):
    competencia = Competencia.objects.get(id=id)
    return render(request, 'portfolio/competencia.html', {'competencia': competencia})

def tfcs_view(request):
    tfcs = Tfc.objects.all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def tfc_view(request, id):
    tfc = Tfc.objects.get(id=id)  
    return render(request, 'portfolio/tfc.html', {'tfc': tfc})


def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def projeto_view(request, id):
    projeto = Projeto.objects.get(id=id)  
    return render(request, 'portfolio/projeto.html', {'projeto': projeto})

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def makingofs_view(request):
    makingofs = MakingOf.objects.all()
    return render(request, 'portfolio/makingofs.html', {'makingofs': makingofs})


def eventos_view(request):
    eventos = Evento.objects.all()
    return render(request, 'portfolio/eventos.html', {'eventos': eventos})

def evento_view(request, id):
    evento = Evento.objects.get(id=id)  
    return render(request, 'portfolio/evento.html', {'evento': evento})   


def projeto_novo(request):
    form = ProjetoForm(request.POST or None,request.FILES)

    if form.is_valid():
        form.save()
        return redirect('projetos')

    context = {'form':form}

    return render(request,'portfolio/projeto_novo.html',context)

def tecnologia_novo_view(request):
    form= TecnologiaForm(request.POST or None,request.FILES)

    if form.is_valid():
        form.save()
        return redirect('tecnologias')

    context = {'form':form}

    return render(request, 'portfolio/tecnologia_novos.html', {'form': form})

def competencia_novo_view(request):
    form = CompetenciaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('competencias')
    context={'form':form}
    return render(request,'portfolio/competencia_novo.html',context)
