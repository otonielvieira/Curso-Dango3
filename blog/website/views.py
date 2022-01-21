from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts

# Create your views here.
list_posts = Posts.objects.all()
lista = ['Django', 'Python', 'Flask', 'KIvy', 'Html', "Css", 'Php', 'Java', 'kotin']
data = {'name': 'Curso de Django, Renderizando Templates', 'lista_tecnologias': lista, 'result': list_posts}

def site(request):
    return render(request, 'index.html', data)