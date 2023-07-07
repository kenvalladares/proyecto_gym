# Generated by Django 4.0.5 on 2023-07-07 15:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym1', '0021_planilla'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoBono',
            fields=[
                ('idTipoBono', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipoBono', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$', 'No puede ingresar números a este campo.'), django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Tipo Bono')),
                ('descripcionTipoBono', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$', 'No puede ingresar números a este campo.'), django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo Bono',
                'verbose_name_plural': 'Tipo Bonos',
            },
        ),
        migrations.CreateModel(
            name='CargoEmpleado',
            fields=[
                ('idCargoEmpleado', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Cargo Empleado')),
                ('fechaInicial', models.DateField(verbose_name='Fecha Inicial')),
                ('fechaFinal', models.DateField(blank=True, null=True, verbose_name='Fecha Final')),
                ('idCargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.cargo', verbose_name='Cargo')),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.empleado', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Cargo Empleado',
                'verbose_name_plural': 'Cargo Empleado',
            },
        ),
        migrations.CreateModel(
            name='Bono',
            fields=[
                ('idBono', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10, unique=True, verbose_name='Monto')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.empleado', verbose_name='Empleado')),
                ('idPlanilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.planilla', verbose_name='Planilla')),
                ('idTipoBono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.tipobono', verbose_name='TipoBono')),
            ],
            options={
                'verbose_name': 'Bono',
                'verbose_name_plural': 'Bonos',
            },
        ),
    ]
