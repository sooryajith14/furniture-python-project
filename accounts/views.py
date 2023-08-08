from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def register(request):

    if request.method == 'POST':
        x = request.POST['fn']
        y = request.POST['ln']
        z = request.POST['user']
        p = request.POST['email']

        a = request.POST['pass']
        b = request.POST['cpass']
        if a == b:
            if User.objects.filter(email=p).exists():
                messages.error(request, 'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=x, last_name=y, username=z, email=p, password=a)
                user.save()
                print('user created')
                return redirect('/')
        else:
            messages.error(request,'password not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def login(request):

    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request,'user not found')
            return redirect('login')
    return render(request,'accounts/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def forgotpassword(requset):
    return render(requset,'accounts/forgotpassword.html')