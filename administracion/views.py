#Importamos las operaciones para renderisar y redirigir
from django.shortcuts import render, redirect
#Importamos el paquete para proteger nuestras vistas de usuarios no registrados (Basadas en funciones)
from django.contrib.auth.decorators import login_required
#Importamos el paquete del Formulario de usuario
from django.contrib.auth.forms import UserCreationForm
#Importamos el paquete para proteger nuestras vistas de usuarios no registrados (Basas en clases)
from django.contrib.auth.mixins import LoginRequiredMixin
#Importamos las vistas genericas
from django.views import generic
#Importamos el modelo User 
from django.contrib.auth.models import User
#Importamos las clases de los modelos que se utilizaran
from .models import Paciente,PersonalHospital,Expediente
#Importamos los formularios
from .forms import PacienteForm,PersonalForm,ExpedienteForm

#Create your views here.

def inicio(request):
    return render(
        request,
        'inicio.html',
    )

def pacientes(request):
    return render(
        request,
        'pacientes.html'
    )

def personal(request):
    return render(
        request,
        'personal.html'
    )

def acercade(request):
    return render(
        request,
        'acercade.html'
    )

#Decorador para proteger la vista de usuarios no registrados
@login_required
#Vista para agregar un nuevo Paciente
def pacientec(request):
    #Comprobamos que se hayan enviado los datos
    if request.method == 'POST':
        #Obtenemos los datos
        formularioPa = PacienteForm(request.POST)
        #Comprobamos que los datos sean validos
        if formularioPa.is_valid():
            #Guardamos el paciente nuevo
            instanciaPa = formularioPa.save(commit=False)
            instanciaPa.save()
            print('Paciente %', str(instanciaPa.id))
            # Después de guardar redireccionamos a la lista
            #return redirect('expedientec/'+str(instanciaPa.id))
            return redirect('expedientec',str(instanciaPa.id))
    #Renderizamos el formulario
    else:
        formularioPa = PacienteForm()
    return render(
        request,
        'formularios/pacientec.html',
        {'formularioPa':formularioPa}
    )

#Decorador para proteger la vista de usuarios no registrados
@login_required
def pacientel(request):
    pacientes = Paciente.objects.all()

    return render(
        request,
        'formularios/pacientel.html',
        {'pacientes':pacientes}
    )

#Decorador para proteger la vista de usuarios no registrados
@login_required
def pacientee(request, paciente_id):
    # Recuperamos la instancia del paciente
    instanciaPa = Paciente.objects.get(id=paciente_id)
    # Creamos el formulario con los datos de la instancia
    formularioInicial = PacienteForm(instance=instanciaPa)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        formularioInicial = PacienteForm(request.POST, instance=instanciaPa)
        # Si el formulario es válido...
        if formularioInicial.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instanciaPa = formularioInicial.save(commit=False)
            # Podemos guardarla cuando queramos
            instanciaPa.save()
            return redirect('pacientel')
    # Si llegamos al final renderizamos el formulario
    return render(
                request,
                "formularios/pacientee.html",
                {'formularioInicial': formularioInicial}
            )

#Decorador para proteger la vista de usuarios no registrados
@login_required
def pacienteb(request,paciente_id):
    # Recuperamos la instancia del personal y la borramos
    instanciaPa = Paciente.objects.get(id=paciente_id)
    instanciaPa.delete()
    # Después redireccionamos de nuevo a la lista
    return redirect(
                'pacientel'
            )

#Decorador para proteger la vista de usuarios no registrados
@login_required
#Vista para agregar un nuevo Personal
def personalc(request,usuario_id):
    #Recuperamos la instancia del usuario al que correspones el personal
    instanciaU = User.objects.get(id=usuario_id)
    #Comprobamos que se hayan enviado los datos
    if request.method == 'POST':
        #Obtenemos los datos
        formularioPer = PersonalForm(request.POST)
        #Comprobamos que los datos sean validos
        if formularioPer.is_valid():
            #Guardamos los datos en una instancia
            instanciaPer = formularioPer.save(commit=False)
            #Establecemos el usuario_id para la relacion OneToOne
            instanciaPer.User = instanciaU
            #Guardamos los datos
            formularioPer.save()
            # Después de guardar redireccionamos a la lista
            return redirect('personall')
    #Renderizamos el formulario
    else:
        formularioPer = PersonalForm()
    return render(
        request,
        'formularios/personalc.html',
        {'formularioPer':formularioPer}
    )

#Decorador para proteger la vista de usuarios no registrados
@login_required
def personale(request, personal_id):
    # Recuperamos la instancia del personal
    instanciaPH = PersonalHospital.objects.get(id=personal_id)
    # Creamos el formulario con los datos de la instancia
    formularioInicial = PersonalForm(instance=instanciaPH)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        formularioInicial = PersonalForm(request.POST, instance=instanciaPH)
        # Si el formulario es válido...
        if formularioInicial.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instanciaPH = formularioInicial.save(commit=False)
            # Podemos guardarla cuando queramos
            instanciaPH.save()
            return redirect('personall')
    # Si llegamos al final renderizamos el formulario
    return render(
        request,
        "formularios/personale.html",
        {'formularioInicial': formularioInicial}
    )

#Decorador para proteger la vista de usuarios no registrados
@login_required
def personalb(request,personal_id):
    # Recuperamos la instancia del personal y la borramos
    instanciaPH = PersonalHospital.objects.get(id=personal_id)
    instanciaPH.delete()
    # Después redireccionamos de nuevo a la lista
    return redirect('personall')

#Decorador para proteger la vista de usuarios no registrados
@login_required
def personall(request):
    personalH = PersonalHospital.objects.all()

    return render(
        request,
        'formularios/personall.html',
        {'personalH':personalH}
    )

#Decorador para proteger la vista de usuarios no registrados
@login_required
#Vista para agregar un nuevo Expediente
def expedientec(request,paciente_id):
    #Recuperamos la instancia del paciente a la que corresponde el expediente
    instanciaPa = Paciente.objects.get(id=paciente_id)
    #Comprobamos que se hayan enviado los datos
    if request.method == 'POST':
        formularioEx = ExpedienteForm(request.POST)
        #Comprobamos que los datos sean validos
        if formularioEx.is_valid():
            #Guardamos los datos en una instancia
            instanciaEx = formularioEx.save(commit=False)
            #Establecemos el paciente_id para la llave foranea
            instanciaEx.Paciente = instanciaPa
            #Guardamos los datos
            instanciaEx.save()
            # Después de guardar redireccionamos a la lista
            return redirect('pacientel')
    #Renderizamos el formulario
    else:
        formularioEx = ExpedienteForm()
    return render(
        request,
        'formularios/expedientec.html',
        {'formularioEx':formularioEx}
    ) 

#Decorador para proteger la vista de usuarios no registrados
@login_required
def expediente(request,paciente_id):
    #instancia
    return render(
        request,
        "formularios/expediente.html"
        #{'formularioInicial': formularioInicial}
    )

class PacientesPorMedico(LoginRequiredMixin,generic.ListView):
    model = Paciente
    template_name ='pacientesMed.html'
    paginate_by = 10
    
    def get_queryset(self):
        personal_id = PersonalHospital.objects.get(User=self.request.user.id)
        return Paciente.objects.filter(Doctor=personal_id.id)

@login_required
def registroU(request):
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        formularioU = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if formularioU.is_valid():
            #Creamos una instancia de usuario
            instanciaUsuario = formularioU.save(commit=False)
            # Creamos la nueva cuenta de usuario
            user = instanciaUsuario.save()
            # Si el usuario se crea correctamente
            return redirect('personalc',str(instanciaUsuario.id))
    else:
        # Creamos el formulario de autenticación vacío
        formularioU = UserCreationForm()
    # Si llegamos al final renderizamos el formulario
    return render(
        request,
        "registration/registro.html",
        {'formularioU': formularioU}
    )