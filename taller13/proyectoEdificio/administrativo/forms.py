from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, Departamento
        

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
            'tipo': _('Ingrese tipo por favor'),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        #El nombre de la ciudad no puede iniciar con la letra mayúscula L
        if valor[0] == "L":
            raise forms.ValidationError("El nombre de la ciudad no puede iniciar con la letra mayúscula L")
        return valor

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'num_cuartos', 'edificio']
        labels = {
                'nombre_propietario': _('Ingrese nombre del propietario por favor'),
                'costo': _('Ingrese el costo por favor'),
                'numero_cuartos': _('Ingrese el numero de cuartos por favor'),
                'edificio': _('Elija un edificio'),
            }

    #Costo de un departamento no puede ser mayor a $100 mil.
    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 100000:
            raise forms.ValidationError("El costo del departamento no puede ser mayor a $100 mil.")
        return valor
    #Número de cuartos no puede ser 0, ni mayor a 7
    def clean_num_cuartos(self):
        valor = self.cleaned_data['num_cuartos']
        if valor == 0:
            raise forms.ValidationError("El número de cuartos no puede ser 0.")
        if valor > 7:
            raise forms.ValidationError("El número de cuartos no puede ser mayor a 7.")
        return valor
    
    #El nombre completo de un propietario no debe tener menos de 3 palabras.
    def clean_nombre_propietario(self):
        valor = self.cleaned_data['nombre_propietario']
        num_palabras = len(valor.split())
        if num_palabras < 3:
            raise forms.ValidationError("Ingrese un nombre y dos apellidos por favor")
        return valor

class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'num_cuartos', 'edificio']
