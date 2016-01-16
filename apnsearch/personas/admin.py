from django.contrib import admin
from django.contrib.auth.models import User, Group
from personas.models import Persona, ConsejoRegional

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('CPsP', 'nombres', 'apellidos', 'fecha_incorporacion', 'telefono')

admin.site.register(ConsejoRegional)
admin.site.unregister(User)
admin.site.unregister(Group)
