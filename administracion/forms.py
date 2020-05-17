#Importamos el ModelForm para el manejo de los formularios
from django import forms
#Importamos las vistas
from .models import Paciente,PersonalHospital,Expediente
#Importamos para realizar consultas
from django.db.models import Q

#Creamos el formulario para el modelo Paciente
class PacienteForm(forms.ModelForm):
    #Doctor = forms.ModelChoiceField(queryset=PersonalHospital.objects.filter(Q(tipoPH='general')|Q(tipoPH='especialista')|Q(tipoPH='diagnostico')))
    def __init__(self,*args,**kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.fields['Doctor'].queryset = PersonalHospital.objects.filter(Q(tipoPH='general')|Q(tipoPH='especialista')|Q(tipoPH='diagnostico'))
    
    class Meta:
        model = Paciente
        #Seleccionamos los campos de forma manual
            #fields = ['numSeguro','nombrePa','apellidoPPa','fechaNaPa','direccionPa',
            #            'sexoPa','numTelPa','habitacion','Doctor']
        
        #Podemos seleccionar todos y solo escluir uno. En este caso FechaIng
        exclude = ['fechaIng']

        help_texts = {
            'numSeguro': None,'nombrePa': None,'apellidoPPa': None,'fechaNaPa': None,
            'direccionPa': None,'sexoPa': None,'numTelPa': None,'habitacion': None,'Doctor': None,
        }

#Creamos el formulario para el Personal
class PersonalForm(forms.ModelForm):
    class Meta:
        model = PersonalHospital
        #fields = '__all__'
        exclude = ['User']

        help_texts = {
            'numMatricula': None,'nombrePH': None,'apellidoPPH': None,'fechaNaPH': None,'direccionPH': None,
            'sexoPH': None,'numTelPH': None,'tipoPH': None,
        }

#Creamos el formulario para el Expediente
class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        #fields = '__all__'
        #widgets = {'Paciente': forms.HiddenInput()}
        exclude = ['Paciente']

        help_texts = {
            'signosVitales': None,'resumenInterrogatorio': None,'exploracionFisica': None,'resultadosEstudios': None,
            'diagnostico': None,'planTratamiento': None,'pronostico': None,'enfermedad': None,
        }