from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name = 'inicio'),
    path('pacientes/',pacientes, name ='pacientes'),
    path('personal/',personal, name ='personal'),
    path('acercade/',acercade, name ='acercade'),
    path('pacientec/',pacientec, name ='pacientec'),
    path('pacientel/',pacientel, name ='pacientel'),
    path('pacientee/<int:paciente_id>',pacientee, name ='pacientee'),
    path('pacienteb/<int:paciente_id>',pacienteb, name ='pacienteb'),
    path('personalc/<int:usuario_id>',personalc, name ='personalc'),
    path('registro/',registroU, name ='registroU'),
    path('personall/',personall, name ='personall'),
    path('personale/<int:personal_id>',personale, name ='personale'),
    path('personalb/<int:personal_id>',personalb, name ='personalb'),
    path('expediente/<int:paciente_id>',expediente, name ='expediente'),
    path('expedientec/<int:paciente_id>',expedientec, name ='expedientec'),
    #Redirigimos las peticiones para poder acceder a los pacientes por usuario (doctor)
    path('mispacientes/', PacientesPorMedico.as_view(), name='mispacientes'),
]