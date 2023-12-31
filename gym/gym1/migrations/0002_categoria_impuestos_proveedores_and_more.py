# Generated by Django 4.0.5 on 2023-07-03 16:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCategoria', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$', 'No puede ingresar números a este campo.'), django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Categoria')),
                ('descripcionCategoria', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$', 'No puede ingresar números a este campo.'), django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Impuestos',
            fields=[
                ('idImpuesto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Impuesto')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('fechaInicial', models.DateField(verbose_name='Fecha Inicial')),
                ('fechaFinal', models.DateField(blank=True, null=True, verbose_name='Fecha Final')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, unique=True, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Impuesto',
                'verbose_name_plural': 'Impuestos',
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('idProveedor', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreProveedor', models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Nombre')),
                ('Direccion', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Dirección')),
                ('Contacto', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^[[2,3,7,8,9]{1}[0-9]{3}[0-9]{4}]*$', 'No puede ingresar letras en este campo, este campo debe comenzar con 2,3,8,9, este campo debe tener 8 digitos'), django.core.validators.RegexValidator('^[0-9 ]*$', 'No puede ingresar letras a este campo.')], verbose_name='Número telefónico')),
                ('rtnProveedor', models.CharField(help_text='formato xxxx-xxxx-xxxxx', max_length=50, validators=[django.core.validators.RegexValidator('^[0-9 ]*$', 'No puede ingresar letras a este campo.'), django.core.validators.RegexValidator('^[[01,10]{1}[0-9]{3}[0-9]{10}]*$', 'No puede ingresar letras en este campo, este campo debe comenzar con 0 o 1, este campo debe tener 14 digitos')], verbose_name='RTN')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.AlterField(
            model_name='generopersona',
            name='nombreGenero',
            field=models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$', 'No puede ingresar números a este campo.'), django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Genero'),
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Nombre de Producto')),
                ('descripcion', models.CharField(max_length=2000, validators=[django.core.validators.RegexValidator('^(?!.*(\\w)\\1{2,}).+$', 'No se pueden ingresar letras repetidas más de 2 veces')], verbose_name='Descripción')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Descuento')),
                ('stockMinimo', models.IntegerField(verbose_name='Stock Mínimo')),
                ('stockMaximo', models.IntegerField(verbose_name='Stock Máximo')),
                ('imagenProducto', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen de Producto')),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.categoria', verbose_name='Categoria')),
                ('idImpuesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym1.impuestos', verbose_name='Impuesto')),
                ('idProveedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.proveedores', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
