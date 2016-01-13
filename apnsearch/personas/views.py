import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from .models import Persona, ConsejoRegional


def index(request):
    return render_to_response("index.html", {}, context_instance=RequestContext(request))

def buscar_persona(request):
    if request.method == 'POST':
        CPsP = request.POST["CPsP"]
        nombres = request.POST["nombres"]
        apellidos = request.POST["apellidos"]

        if CPsP:
            personas = Persona.objects.filter(CPsP=CPsP)
        else:
            personas = Persona.objects.filter(nombres__contains=nombres) |\
                Persona.objects.filter(apellidos__contains=apellidos)

        response_data = [
            {
                "CPsP": p.CPsP,
                "nombres" : p.nombres,
                "apellidos" : p.apellidos,
                "telefono": p.telefono,
                "fecha_incorporacion": str(p.fecha_incorporacion),
                "email": p.email,
                "foto": p.foto.url,
                "consejo_regional": p.consejo_regional.nombre,
                "direccion": p.direccion,
                "telefono": p.telefono,
            }
            for p in personas
        ]

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't hapenning"}),
            content_type="appliction/json"
        )
