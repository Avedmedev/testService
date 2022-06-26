

from django.shortcuts import render


def index(request):
    context = {'title': 'Main page'}
    return render(request, 'myTest\index.html', context=context)    