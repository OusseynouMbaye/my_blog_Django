from django.shortcuts import render
from datetime import datetime


def index(request):
    day = datetime.today()
    return render(request, 'MyBlog/index.html', context={
        'Name': 'Amina',
        'date': day
    })
