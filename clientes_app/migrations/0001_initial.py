# Generated by Django 5.1.2 on 2024-12-03 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=255)),
                ('F_nacimiento', models.DateField(blank=True, null=True)),
                ('Telefono', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=255)),
                ('Direccion', models.TextField()),
            ],
        ),
    ]
