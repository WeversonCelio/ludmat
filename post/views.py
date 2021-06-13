from django.shortcuts import render
from django.http import HttpResponse
from post.models import Anterior, Materia, Proxima
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


def post(request,id):
    # buscar os atributos no banco de dado da materia
    materiaDb = Materia
    todasMaterias = materiaDb.objects.all()
    elemento = todasMaterias.get(id=id)

    titulo = "POST " + str(elemento.id) + " | " + elemento.titulo

    # buscar os atributos no banco de dado da materia relacionadas
    anteriorDb = Anterior
    todasAnterior = anteriorDb.objects.all()
    anteriorId = todasAnterior.get(anterior=id)
    anteriorPost = todasMaterias.get(id=anteriorId.id)

    # buscar os atributos no banco de dado da materia relacionadas
    proximoDb = Proxima
    todosProximos = proximoDb.objects.all()
    proximoId = todosProximos.get(proximo=id)
    proximoPost = todasMaterias.get(id=proximoId.id)


    # enviar comentario via e-mail
    if request.method == 'POST':
        mensagem = "Comentario do Post " + str(elemento.id) + " - " + elemento.titulo  + "\n" 
        mensagem +="Nome: "+request.POST['nome']+"\n"
        mensagem +="Comentario: "+request.POST['mensagem']+"\n"
        send_mail(
            'Comentario LudMat:',
            mensagem,
            'from@example.com',
            ['weversoncelio25@gmail.com'],
            fail_silently=False,
        )

    
    
    context = {
        'title': titulo,
        'page' : "index",
        'todasMaterias' : todasMaterias,
        'elemento' : elemento,
        'anterior' : anteriorPost,
        'proximo' : proximoPost
    }
    return render(request,"post/post.html", context)