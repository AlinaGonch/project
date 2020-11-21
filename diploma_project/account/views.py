from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators   import login_required

from .forms import CreateUserForm

@login_required(login_url='log_page')
def personal_page(request):
    pass

def reg_page(request):
    # if request.user.is_authenticed:
    #     return redirect('home')
    # else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'Account was created by' + user)
               return redirect('log_page')

        return render(request, 'register.html', {'form': form} )


def log_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User or Password was not given')

    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('log_page')

# Create your views here.

