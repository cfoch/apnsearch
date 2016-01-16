import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from .models import Persona, ConsejoRegional


def index(request):
    if request.method == 'POST':
        CPsP = request.POST["CPsP"]
        nombres = request.POST["nombres"]
        apellidos = request.POST["apellidos"]

        personas = []
        try:
            print("jere")
            if CPsP:
                personas = Persona.objects.filter(CPsP=CPsP)
            elif nombres or apellidos:
                personas = Persona.objects.filter(
                    nombres__icontains=nombres
                ).filter(apellidos__icontains=apellidos)
            print(personas)
        except:
            pass

        context_data = {"personas": personas}
        if personas:
            context_data["persona"] = personas[0]
        

        return render_to_response("resultados.html", context_data,
            context_instance=RequestContext(request))
    else:
        return render_to_response("base.html", {},
            context_instance=RequestContext(request))

def actualizar_tarjeta(request):
    ret = HttpResponse(
        json.dumps({"nothing to see": "this isn't hapenning"}),
        content_type="appliction/json"
    )
    if request.method == 'POST':
        CPsP = request.POST["CPsP"]

        try:
            p = Persona.objects.get(CPsP=CPsP)
        except:
            return ret

        if p.foto:
            foto_url = p.foto.url
        else:
            foto_url = ''

        response_data = {
            "CPsP": p.CPsP,
            "nombres" : p.nombres,
            "apellidos" : p.apellidos,
            "telefono": p.telefono,
            "fecha_incorporacion": str(p.fecha_incorporacion),
            "email": p.email,
            "foto": foto_url ,
            "consejo_regional": p.consejo_regional.nombre,
            "direccion": p.direccion,
            "telefono": p.telefono,
        }

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    return ret
        
