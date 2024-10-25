from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os

def app(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def peticion_donacion(request):

    return render(request, "registro.html")

def donar(request):
    
    mensaje="Registro donacion: %r" %request.GET["dnd"]
    return HttpResponse(mensaje)

def registro(request):

    if request.method == "POST":
         
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")

        return HttpResponse("Formulario completado exitosamente")
    return render(request, "home.html")

def donacion(request):

    return render(request, "donaciones.html")






# Create your views here.
