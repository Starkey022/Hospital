#Importamos el modelo User 
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#Declaramos los modelos que utilizaremos dentro de la base de datos

#Declaramos el modelo Personal
class PersonalHospital(models.Model):
#class PersonalHospital(User):
    #numMatricula = models.IntegerField(help_text="Ingrese la matricula:")
    
    #Definimos las opciones para el tipo de Personal
    PERSONAL_OP = [
        ('Personal_Medico',(
            ('general','General'),
            ('especialista','Especialista'),
            ('cirujano','Cirujano'),
            ('diagnostico','Diagnostico'),
         )
        ),
        ('Personal_Administrativo',(
            ('secretaria','Secretaria'),
            ('archivista','Archivista'),
            ('almacenista','Almacenista'),
            ('oficinista','Oficinista'),
         )
        ),
        ('Personal_Paramedico',(
            ('enfermero','Enfermero'),
         )
        ),
    ]

    SEXO_OP = [
        ('masculino','Masculino'),
        ('femenino','Femenino'),
    ]

    #Extendemos el modelo Usuario
    User = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    #Establecemos la llave primaria del modelo
    numMatricula = models.IntegerField('Matricula',help_text="Ingrese la matricula:")
    nombrePH = models.CharField('Nombre',max_length=30,help_text="Ingrese el nombre:")
    apellidoPPH = models.CharField('Apellido',max_length=30,help_text="Ingrese el apellido:")
    fechaNaPH = models.DateField('Fecha de nacimiento')
    direccionPH = models.CharField('Direccion',max_length=50,help_text="Ingrese la direccion:")
    sexoPH = models.CharField('Sexo', choices=SEXO_OP,max_length=20,help_text="Ingrese el sexo:")
    numTelPH = models.IntegerField('Numero de telefono',help_text="Ingrese su numero telefonico:")
    #Revisar el tipo de personal, solo se podran elegir 3 tipos
    tipoPH = models.CharField('Tipo de empleado',max_length=20,choices=PERSONAL_OP,help_text="Ingrese tipo de empleado:")

    class Meta:
        verbose_name = 'Personal Medico'
        verbose_name_plural = 'Personal Medico'

    def __str__(self):
        return "%s %s (%s)" % (self.nombrePH,self.apellidoPPH,self.tipoPH)


#Declaramos al modelo del Paciente
class Paciente(models.Model):
    SEXO_OP = [
        ('masculino','Masculino'),
        ('femenino','Femenino'),
    ]
    #numSeguro = models.IntegerField(help_text="Ingrese el Numero de Seguro:")
    numSeguro = models.IntegerField('Numero de seguro')
    nombrePa = models.CharField('Nombre',max_length=30)
    apellidoPPa = models.CharField('Apellido',max_length=30)
    fechaNaPa = models.DateField('Fecha de nacimiento')
    direccionPa = models.CharField('Direccion',max_length=50,help_text="Ingrese la direccion:")
    fechaIng = models.DateField('Fecha de ingreso',auto_now=False,auto_now_add=True)
    sexoPa = models.CharField('Sexo',max_length=20,choices=SEXO_OP,help_text="Ingrese el sexo:")
    numTelPa = models.IntegerField('Numero de telefono',help_text="Ingrese su numero telefonico:")
    habitacion = models.CharField('Habitacion',max_length=4,help_text="Ingrese la habitacion:")
    #Establecemos la relacion con el doctor encargado
    Doctor = models.ForeignKey(PersonalHospital,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return "%s %s" % (self.nombrePa,self.apellidoPPa)
    
#Declaramos el modelo Expediente
class Expediente(models.Model):
    #Establecemos la llave primaria del modelo
    #numExpediente = models.IntegerField(ax_length=30,)
    signosVitales = models.CharField('Signos vitales',max_length=200,help_text="Signos vitales del paciente:")
    resumenInterrogatorio = models.CharField('Resumen del interrogatorio',max_length=600,help_text="Resumen del interregotario medico:")
    exploracionFisica = models.CharField('Exploracion fisica',max_length=600,help_text="Resultado de la revision fisica del paciente:")
    resultadosEstudios = models.CharField('Resultados de los estudios',max_length=600,help_text="Resultados de los estudios practicados:")
    diagnostico = models.CharField('Diagnostico',max_length=600,help_text="Diagnostico del medico:")
    planTratamiento = models.CharField('Plan de tratamiento',max_length=600,help_text="Plan asignado para atender al paciente:")
    pronostico = models.CharField('Pronostico',max_length=600,help_text="Pronostico de recuperacion:")
    enfermedad = models.CharField('Enfermedad',max_length=600,help_text="Enfermedades que presenta el paciente:")
    #Establecemos la Llave Foranea con el modelo Paciente
    Paciente = models.OneToOneField(Paciente,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name = 'Expediente'
        verbose_name_plural = 'Expedientes'

    def __str__(self):
        return "Expediente del paciente: %s" % (self.numSeguro)