from django.urls import path
from . import views

urlpatterns = [
    path("", views.app, name ="app"),
    path("app/", views.app, name="app"),
    path("registro/", views.registro, name = "registro"),
    path("donacion/", views.donacion, name = "donacion"),
]
