from post.models import Materia
from django.shortcuts import render

# Create your views here.
def slide(request):
    materiaDb = Materia
    todasMaterias = materiaDb.objects.all()
    
    

    context = {
        'title': "FOTOS",
    }
    return render(request,"slide/slide.html", context)
