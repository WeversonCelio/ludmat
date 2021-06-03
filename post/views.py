from django.shortcuts import render
from django.http import HttpResponse
from post.models import Materia
from django.core.mail import send_mail

# Create your views here.
def index(request):
    materiaDb = Materia
    todasMaterias = materiaDb.objects.all()

  


    context = {
        'title': "HOME",
        'page' : "index",
        'todasMaterias' : todasMaterias
    }
    return render(request,"site/index.html", context)

def sobre(request):
    if request.method == 'POST':
        mensagem = "Dados da Mensagem:\n"
        mensagem +="Nome: "+request.POST['nome']+"\n"
        mensagem +="Email: "+request.POST['email']+"\n"
        mensagem +="Mensagem: "+request.POST['mensagem']+"\n"
        send_mail(
            'Mensagem de Contato LudMat:',
            mensagem,
            'from@example.com',
            ['weversoncelio25@gmail.com'],
            fail_silently=False,
        )


    context = {
        'title': "SOBRE",
        'page' : "sobre"
    }
    return render(request,"site/sobre.html", context)


def post(request):
    materiaDb = Materia
    todasMaterias = materiaDb.objects.all()
    elemento = todasMaterias.get(id=1)
    
    context = {
        'title': "POST",
        'page' : "index",
        'todasMaterias' : todasMaterias,
        'elemento' : elemento
    }
    return render(request,"post/post.html", context)