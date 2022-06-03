from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.
def news_home(request):
    news = Articles.objects
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

@login_required(login_url='login')
def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Форма была неверной"

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)