from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def site(request):
    return HttpResponse('<h1>Hello Main Pagem form main Dajango App<h1>')
