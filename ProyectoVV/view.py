from django.http import HttpResponse
from django.shortcuts import render


def welcome(req):
    # return HttpResponse('Hola mundo')
    return render(req, 'index.html')
