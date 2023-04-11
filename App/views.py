from django.shortcuts import render, redirect
from App.models import inicio
from App.forms import FormularioContacto
from django.core.mail import EmailMessage

def home(request):
    inicio1= inicio.objects.all()
    return render(request, 'App/home.html', {"inicio1": inicio1})

def contacto(request):
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la direccion {} te escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
            "",["lucas.ponto1234@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?NOvalido")
    return render(request, 'App/contacto.html', {'miFormulario':formulario_contacto})





