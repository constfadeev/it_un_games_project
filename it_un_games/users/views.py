from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, '/register.html', context)


def loginPage(request):
    context = {}
    return render(request, '/login.html', context)

# Create your views here.
