from django.shortcuts import render,redirect
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
    if request.method == "GET":
            form = PersonaForm()
            contexto = {
                'form':form
            }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('listarPersona')
    return render(request, 'crearPersona.html',contexto)


def listarPersona(request):
    persona = Persona.objects.all()
    contexto = {'persona' : persona}
    return render (request,'listarPersona.html', contexto)

def editarPersona(request, id_persona):
    persona = Persona.objects.get(id_persona = id_persona)
    if request.method == 'GET':
        form = PersonaForm(instance = persona)
        
    else:
        form = PersonaForm(request.POST, instance = persona)
        if form.is_valid():
            form.save()
        return redirect ('listarPersona')
    return render(request, 'crearPersona.html')


def eliminarPersona(request, id_persona):
    persona = Persona.objects.get(id_persona = id_persona)
    if request.method == 'GET':
        persona.delete()
        return redirect('listarPersona')