from django.contrib import admin
#Importamos los modelos que seran administrables
from .models import Paciente,PersonalHospital,Expediente

# Register your models here.
#Realizamos clases del tipo administracion para poder presentar de mejor forma los
#   modelos administrables

#Clase para administrar a los Pacientes
class PacienteAdmin(admin.ModelAdmin):
    #Creamos una barra de busqueda para poder encontar mejor la informacion
    search_fields = ['numSeguro','nombrePa']
    #Establecemos como queremos que se muestren los datos
        #Falta establecer la fecha en que entra el paciente
    list_display = ('numSeguro','nombrePa','habitacion')
    #Establecemos filtros para poder buscar de mejor forma los pacientes
    filter_display = ('habitacion','apellidoPPa')

#Clase para administrar los Expedientes
class ExpedienteAdmin(admin.ModelAdmin):
    #Creamos una barra de busqueda para poder encontar mejor la informacion
    search_fields = ['Paciente']
    #Establecemos como queremos que se muestren los datos
    list_display = ('Paciente','enfermedad')

#Clase para administrar al Personal
class PersonalHospitalAdmin(admin.ModelAdmin):
    #Creamos una barra de busqueda para poder encontar mejor la informacion
    search_fields = ['numMatricula','nombrePH','apellidoPPH']
    #Establecemos como queremos que se muestren los datos
    list_display = ('nombrePH','apellidoPPH','numMatricula')

#Registramos la admin class con el modelo asociado
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Expediente, ExpedienteAdmin)
admin.site.register(PersonalHospital, PersonalHospitalAdmin)