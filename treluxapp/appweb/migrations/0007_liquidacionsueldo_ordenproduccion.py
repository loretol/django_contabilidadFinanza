# Generated by Django 5.0.1 on 2024-01-26 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0006_bodega_puntoventa_ordenrequisicion'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiquidacionSueldo',
            fields=[
                ('id_liquidacion', models.AutoField(primary_key=True, serialize=False)),
                ('Sueldo_Base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Comisiones', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dias_trabajados', models.IntegerField()),
                ('Base_Imponible', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Descuentos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Total_Haberes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Liquido_A_Pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Bonificaciones', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_periodo', models.DateField()),
                ('id_afp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.afp')),
                ('id_salud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.salud')),
                ('rut_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenProduccion',
            fields=[
                ('id_orden_produc', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('productos_usados', models.TextField()),
                ('personal_de_trabajo', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('id_bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.bodega')),
            ],
        ),
    ]
