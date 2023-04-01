from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html') #, {'title': 'Главная страница'}

def addtest(request):
    return render(request, 'main/addtest.html')


# def create(request):
#     return render(request, 'testapp/create.html')