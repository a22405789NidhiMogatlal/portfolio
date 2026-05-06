from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Perfil
import secrets

from django.http import HttpResponse
def login_view(request):
    if request.method=="POST":
        print(request.POST)
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])

        if user:
            login(request,user)
            next_url = request.POST.get('next')

            if next_url:
                return redirect(next_url)
            return redirect('licenciaturas')

        else:
            return render(request,'accounts/login.html',{'mensagem':'Credenciais inválidas'})
        

    return render(request,'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('licenciaturas')

def registo_view(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('licenciaturas')
    
    context={'form':form}
    return render(request,'accounts/registo.html',context)

def envia_email(user, email):

    send_mail(
        subject='Portfolio: Autenticação',

        message=f'''
Olá {user.username},

Clique no link:

http://127.0.0.1:8000/accounts/autentica/?token={user.perfil.token}
''',

        from_email='admin@portfolio.com',

        recipient_list=[email]
    )



def login_magic_link(request):

    email = request.POST.get('email')

    if User.objects.filter(email=email).exists():

        user = User.objects.get(email=email)

        perfil, created = Perfil.objects.get_or_create(user=user)

        perfil.token = secrets.token_urlsafe(32)

        perfil.save()

        envia_email(user, email)

        return HttpResponse("Email enviado com sucesso ")

    return render(
        request,
        'accounts/magic_login.html',
        {'mensagem': 'Email não existe'}
    )
