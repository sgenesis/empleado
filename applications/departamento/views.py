from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView

from applications.persona.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoForm


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'


    def form_valid(self, form):
        print('*********Estamos en el form valid ')

        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['short_name']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job=str('1'),
            departamento= depa
        )
        return super(NewDepartamentoView, self).form_valid(form)

# Create your views here.

