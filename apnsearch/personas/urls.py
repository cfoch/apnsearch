from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^buscar/', views.buscar_persona, name='buscar_persona')
]
