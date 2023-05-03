from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

print()

def index(request):
    return HttpResponse("Olá... Seja bem vindo à enquete")