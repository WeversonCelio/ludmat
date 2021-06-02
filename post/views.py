from django.shortcuts import render
from django.http import HttpResponse
from post.models import Materia

# Create your views here.
def index(request):
    materiaDb = Materia
    todasMaterias = materiaDb.objects.all()

  


    context = {
        'title': "HOME",
        'page' : "index",
        'todasMaterias' : todasMaterias
    }
    return render(request,"post/index.html", context)

def sobre(request):
    context = {
        'title': "SOBRE",
        'page' : "sobre"
    }
    return render(request,"post/sobre.html", context)