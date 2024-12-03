# Generated by Django 5.1.2 on 2024-12-03 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('Id_cliente', models.IntegerField()),
                ('Fecha', models.DateField(blank=True, null=True)),
                ('Id_producto', models.IntegerField()),
                ('Id_Categoria', models.IntegerField()),
                ('Cantidad', models.IntegerField()),
            ],
        ),
    ]