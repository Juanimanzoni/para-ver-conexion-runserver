from datetime import datetime
from django.http import HttpResponse
import datetime
from django.template import Context, Template


def saludar(request):
    return HttpResponse("Hola Mundo")

def segunda_vista(request):
    return HttpResponse('segunda vista')

#def calcula_año_nacimiento(self,edad):
#    return HttpResponse("<h1>Tu año de Nacimiento es :"+str(int(datetime.datetime.now)))
#mi_archivo=open("Proyecto1/Plantillas/template1.html")