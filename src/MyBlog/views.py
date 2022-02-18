from django.shortcuts import render


def index(request):
    print('test ici'),
    return render(request, 'index.html')
