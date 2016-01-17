from django.contrib import admin
from django.contrib.auth.models import User, Group
from personas.models import Persona, ConsejoRegional
from personas.models import Provincia, Distrito, Departamento

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('CPsP', 'nombres', 'apellidos', 'fecha_incorporacion', 'telefono', 'distrito')

admin.site.register(Provincia)
admin.site.register(Distrito)
admin.site.register(Departamento)
admin.site.register(ConsejoRegional)
admin.site.unregister(User)
admin.site.unregister(Group)
