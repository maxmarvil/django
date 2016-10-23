from django.shortcuts import render, redirect
from django.contrib import auth
from django.template.context_processors import csrf

from account.lib.account import Account


def home(request):
    return render(request,'home.html', {})

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        #проверяем пост-запрос на авторизацию
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render(request,"login.html",args)
    else:
        return render(request, "login.html", args)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    return render(request, "register.html", {})

def accountPage(request):
    args = {}
    username = auth.get_user(request).username
    if(username):
        args['username'] = username
        args['fields'] = Account.fields
    else:
        args['username'] = None

    return render(request, 'account.html',{})