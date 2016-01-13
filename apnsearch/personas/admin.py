from django.contrib import admin
from personas.models import Persona, ConsejoRegional

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('CPsP', 'nombres', 'apellidos', 'fecha_incorporacion', 'telefono')

admin.site.register(ConsejoRegional)
