from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def tests_home(request):
    test = Articles.objects.all()
    return render(request, 'testapp/test_home.html', {'test': test})

# def ShowTest(request):

class ShowTest(DetailView):
    model = Articles
    template_name = 'testapp/show_test.html'
    context_object_name = 'article'

def create_test(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tests_home')
        else:
            error = 'Форма заполнена неверно'
    
    form = ArticlesForm
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'testapp/create.html', data)