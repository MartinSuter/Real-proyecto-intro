from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def app(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def peticion_donacion(request):

    return render(request, "registro.html")

def donar(request):
    
    mensaje="Registro donacion: %r" %request.GET["dnd"]
    return HttpResponse(mensaje)
# Create your views here.
