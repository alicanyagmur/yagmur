from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login, logout
# Create your views here.


def Login_View(request):
    form = LoginForm(request.POST or None)
    if request.method =='POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('home')
        else:
            print(request.POST)
            return render(request, 'account/login.html', {'form': form})
    else:
        return render(request,'account/login.html',{'form': form})


def Register_View(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form)
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            user.set_password(password)
            email = form.cleaned_data.get('email')
            user.email = email
            user.username = username
            user.is_staff = False
            user.is_superuser = False

            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request,new_user)
            return redirect('home')

    return render(request, 'account/register.html', {'form': form})



def Logout_View(request):
	logout(request)
	return redirect('post:landing')