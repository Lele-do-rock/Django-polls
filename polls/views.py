from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse

# Create your views here.

print()

def index(request):
    return HttpResponse("Olá... Seja bem vindo à enquete")

def sobre(request):
    return HttpResponse("Olá este é um app de enquete!")
