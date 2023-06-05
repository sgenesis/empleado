from django.http import HttpResponse

def index():
    return HttpResponse('hola desde un archivo python')