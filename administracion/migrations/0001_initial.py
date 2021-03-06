# Generated by Django 3.0.5 on 2020-05-05 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalHospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numMatricula', models.IntegerField(help_text='Ingrese la matricula:')),
                ('nombrePH', models.CharField(help_text='Ingrese el nombre:', max_length=30)),
                ('apellidoPPH', models.CharField(help_text='Ingrese el apellido:', max_length=30)),
                ('fechaNaPH', models.DateField()),
                ('direccionPH', models.CharField(help_text='Ingrese la direccion:', max_length=50)),
                ('sexoPH', models.CharField(help_text='Ingrese el sexo:', max_length=10)),
                ('numTelPH', models.IntegerField(help_text='Ingrese su numero telefonico:')),
                ('tipoPH', models.CharField(choices=[('Personal_Medico', (('general', 'General'), ('especialista', 'Especialista'), ('cirujano', 'Cirujano'), ('diagnostico', 'Diagnostico'))), ('Personal_Administrativo', (('secretaria', 'Secretaria'), ('archivista', 'Archivista'), ('almacenista', 'Almacenista'), ('oficinista', 'Oficinista'))), ('Personal_Paramedico', (('enfermero', 'Enfermero'),))], help_text='Ingrese tipo de empleado:', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numSeguro', models.IntegerField(help_text='Ingrese el numero de seguro:')),
                ('nombrePa', models.CharField(help_text='Ingrese el nombre:', max_length=30)),
                ('apellidoPPa', models.CharField(help_text='Ingrese el apellido:', max_length=30)),
                ('fechaNaPa', models.DateField()),
                ('direccionPa', models.CharField(help_text='Ingrese la direccion:', max_length=50)),
                ('fechaIng', models.DateField(auto_now_add=True)),
                ('sexoPa', models.CharField(help_text='Ingrese el sexo:', max_length=10)),
                ('numTelPa', models.IntegerField(help_text='Ingrese su numero telefonico:')),
                ('habitacion', models.CharField(help_text='Ingrese la habitacion:', max_length=4)),
                ('numDoctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.PersonalHospital')),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signosVitales', models.CharField(help_text='Signos vitales del paciente:', max_length=200)),
                ('resumenInterrogatorio', models.CharField(help_text='Resumen del interregotario medico:', max_length=600)),
                ('exploracionFisica', models.CharField(help_text='Resultado de la revision fisica del paciente:', max_length=600)),
                ('resultadosEstudios', models.CharField(help_text='Resultados de los estudios practicados:', max_length=600)),
                ('diagnostico', models.CharField(help_text='Diagnostico del medico:', max_length=600)),
                ('planTratamiento', models.CharField(help_text='Plan asignado para atender al paciente:', max_length=600)),
                ('pronostico', models.CharField(help_text='Pronostico de recuperacion:', max_length=600)),
                ('enfermedad', models.CharField(help_text='Enfermedades que presenta el paciente:', max_length=600)),
                ('numSeguro', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Paciente')),
            ],
        ),
    ]
