# Generated by Django 4.0.4 on 2022-05-25 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('biografia', models.TextField()),
                ('imagen', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('sinopsis', models.TextField(help_text='De que trata la pelicula', max_length=100)),
                ('duracion', models.PositiveIntegerField(help_text='Cuanto dura la pelicula en minutos')),
                ('imagen', models.URLField()),
                ('anyo', models.PositiveIntegerField(help_text='Año de publicación de la pelicula')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peliculas.director')),
            ],
        ),
    ]
