# Generated by Django 4.0.5 on 2023-07-03 23:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym1', '0006_cargo_tipodocumento_alter_tipodeduccion_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Empleado')),
                ('nombreEmpleado', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$', 'No puede ingresar números a este campo.'), django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Nombre')),
                ('apellidoEmpleado', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$', 'No puede ingresar números a este campo.'), django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Apellido')),
                ('direccion', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Dirección')),
                ('contacto', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[[2,3,7,8,9]{1}[0-9]{3}[0-9]{4}]*$', 'No puede ingresar letras en este campo, este campo debe comenzar con 2,3,8,9, este campo debe tener 8 digitos')], verbose_name='Contacto')),
                ('fechaNacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('fechaIngreso', models.DateField(verbose_name='Fecha de Ingreso')),
                ('documento', models.CharField(blank=True, max_length=50, verbose_name='Documento')),
                ('idCargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.cargo', verbose_name='Cargo')),
                ('idDocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.tipodocumento', verbose_name='Documento')),
                ('idGenero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.generopersona', verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]
