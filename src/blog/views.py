from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'blogapp/index.html')


def article(request, numero_article):
    print(numero_article)
    return render(request, f'blogapp/article_{numero_article}.html')
