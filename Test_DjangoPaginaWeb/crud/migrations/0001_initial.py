# Generated by Django 4.0.5 on 2022-07-14 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
                'ordering': ['-marca'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
                ('precio_unitario', models.IntegerField(verbose_name='Precio Unitario')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos', verbose_name='Imagen')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.marca')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'ordering': ['idProducto'],
            },
        ),
        
    ]
