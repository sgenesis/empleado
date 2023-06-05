from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = ('titulo', 'subtitulo')

        widgets = {
            'titulo' : forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese texto aqui'
                }
            )
        }

    def clean_titulo(self):
        titulo = self. cleaned_data['titulo']
        if len(titulo) < 10:
            raise forms.ValidationError('Ingrese un titulo con almenos 10 caracteres')
        return titulo