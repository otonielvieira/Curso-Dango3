from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts
from .models import Contato

# Create your views here.
list_posts = Posts.objects.all()
lista = ['Django', 'Python', 'Flask', 'KIvy', 'Html', "Css", 'Php', 'Java', 'kotin']
data = {'name': 'Curso de Django, Renderizando Templates', 'lista_tecnologias': lista, 'posts': list_posts}

def site(request):
    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Posts.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})


def save_form(request):
    name=request.POST['name']
    Contato.objects.create(
        name=name,
        email=request.POST['email'],
        message=request.POST['message'],
         )
    return render(request,'contato.html', {'name_contato': name})