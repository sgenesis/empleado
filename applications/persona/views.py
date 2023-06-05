from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

# 1.-  Lista todos los empleados de la empresa
# 2.-  Listar todos los empleados que pertenezcan a un área de una empresa
# 3.-  Listar empleados por trabajo
# 4.-  Listar los empleados por palabra clave
# 5.-  Listar habilidades del empleado
from .models import Empleado
from .forms import EmpleadoForm

class InicioView(TemplateView):
    '''Vista que carga la pagina de inicio '''
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista =Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

    
class ListByAreaEmpleado(ListView):
    '''Lista de empleados por area'''
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
            departamento__name= area)
        return lista
    
class ListEmpleadosByKword(ListView):
    ''' Lista empleados palabra clave'''
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('*********************')
        palabra_clave = self.request.GET.get('kword', '')
        print('=======', palabra_clave)
        lista =Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista
    
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=8)
        return empleado.habilidades.all()
    
'''Este tipo de vista se utiliza para mostrar tablas detallas de información en este caso de nuestro empleado'''
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccesView(TemplateView):
    template_name = 'persona/success.html'

'''El create view nos crea automaticamente un formulario de los datos para registrar'''

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'avatar'
        'habilidades',
        'hoja_vida',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(f'{"*"*10}Metodo post{"*"*10}')
        print(f'{"="*10}')
        print(request.POST)
        print(request.POST['last_name'])
        print(f'{"*"*30}')
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #logica del proceso
        print(f'{"*"*10}Metodo form valid{"*"*10}')
        print(f'{"*"*25}')
        return super(EmpleadoUpdateView, self).form_valid(form)
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')