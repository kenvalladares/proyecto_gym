# Generated by Django 4.0.5 on 2023-07-06 20:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym1', '0017_alter_ejerciciosrutina_idtipomaquina_rutina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('idSalon', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSalon', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$', 'No puede ingresar números a este campo.'), django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Salon')),
                ('descripcionSalon', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$', 'No puede ingresar números a este campo.'), django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Salon',
                'verbose_name_plural': 'Salon',
            },
        ),
        migrations.AlterField(
            model_name='rutina',
            name='fechaFinal',
            field=models.DateField(null=True, verbose_name='Fecha Final'),
        ),
    ]
