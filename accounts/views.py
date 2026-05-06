from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def login_view(request):
    if request.method=="post":
        user=authenticate(request,username=request.POST['username'],password=request.POST['passoword'])

        if user:
            login(request,user)
            return redirect('licenciaturas')
        else:
            return render(request,'accounts/login.html',{'mensagem':'Credenciais inválidas'})
        
        return render(request,'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('licenciaturas')

def registo(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('licenciaturas')
    
    context={'form':form}
    return render(request,'accounts/registo.html',context)



