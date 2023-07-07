# Generated by Django 4.0.5 on 2023-07-06 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym1', '0019_clases'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClasesCliente',
            fields=[
                ('idClasesCliente', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicial', models.DateField(verbose_name='Fecha Inicial')),
                ('fechaFinal', models.DateField(null=True, verbose_name='Fecha Final')),
                ('idClases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.clases', verbose_name='Clases')),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym1.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Clases Clientes',
                'verbose_name_plural': 'Clases Clientes',
            },
        ),
    ]
