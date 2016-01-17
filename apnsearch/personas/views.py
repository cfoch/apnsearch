import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from .models import Persona, ConsejoRegional
from personas.models import Provincia, Distrito, Departamento


def index(request):
    departamentos = Departamento.objects.all()
    context_data = {"departamentos": departamentos}
    if request.method == 'POST':
        CPsP = request.POST["CPsP"]
        nombres = request.POST["nombres"]
        apellidos = request.POST["apellidos"]
        try:
            distrito_pk = int(request.POST["distrito"])
            distrito = Distrito.objects.get(pk=distrito_pk)
        except:
            distrito = None

        personas = []
        if CPsP:
            personas = Persona.objects.filter(CPsP=CPsP)
        elif nombres or apellidos:
            personas = Persona.objects.filter(
                nombres__icontains=nombres
            ).filter(apellidos__icontains=apellidos)
        if distrito:
            if personas:
                personas = personas.filter(distrito=distrito)
            else:
                personas = Persona.objects.filter(distrito=distrito)

        context_data["personas"] = personas
        if personas:
            context_data["persona"] = personas[0]        

        return render_to_response("resultados.html", context_data,
            context_instance=RequestContext(request))
    else:

        if "departamento" in request.GET:
            pk_departamento = request.GET["departamento"]
            try:
                departamento = Departamento.objects.get(pk=pk_departamento)
                provincias = Provincia.objects.filter(departamento=departamento)
                context_data["departamento"] = departamento
                context_data["provincias"] = provincias
            except ValueError or Departamento.DoesNotExist:
                pass
        elif "provincia" in request.GET:
            pk_provincia = request.GET["provincia"]
            try:
                provincia = Provincia.objects.get(pk=pk_provincia)
                distritos = Distrito.objects.filter(provincia=provincia)
                departamento = provincia.departamento
                provincias = Provincia.objects.filter(departamento=departamento)
                context_data["departamento"] = departamento
                context_data["provincia"] = provincia
                context_data["provincias"] = provincias
                context_data["distritos"] = distritos
            except ValueError or Provincia.DoesNotExist:
                pass
        print(context_data)
        return render_to_response("base.html", context_data,
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
        
