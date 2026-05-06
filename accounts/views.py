from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

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



