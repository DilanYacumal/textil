from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from .forms import PersonaForm
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.
def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar(request):
    if request.method == "POST":
        asunto = request.POST[ "txtAsunto"]
        mensaje = request.POST[ "txtMensaje"] + "Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["dildpizo@misena.edu.co"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")


def home(request):
    return render(request, 'index.html')

def crearPersona(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return('index')
    else:
        form = PersonaForm()
    return render(request, 'crearPersona.html', {'form':form})
