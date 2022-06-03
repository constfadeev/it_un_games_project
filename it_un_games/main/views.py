from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + ", ты успешно зарегестрировался!")
                return redirect('login')
        context = {'form': form}
        return render(request, 'main/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('main/login.html')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST['next'])
                return redirect('home')
            else:
                messages.info(request, 'Логин или пароль неверны')

        context = {}

        return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def index(request):
    return render(request, 'main/about.html')

def about(request):
    return render(request, 'main/about.html')

#class RegisterUser(DataMixin, CreateView):
