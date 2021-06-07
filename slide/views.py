from django.shortcuts import render

# Create your views here.
def slide(request):
    context = {
        'title': "FOTOS",
    }
    return render(request,"slide/slide.html", context)
