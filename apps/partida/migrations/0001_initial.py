# Generated by Django 3.2.8 on 2021-10-21 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ingreso', models.CharField(max_length=5)),
                ('carta_des', models.PositiveIntegerField(blank=True, null=True)),
                ('carta_mod', models.PositiveIntegerField(blank=True, null=True)),
                ('carta_err', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador_numero', models.CharField(choices=[('jugador 1', 'jugador 1'), ('jugador 2', 'jugador 2'), ('jugador 3', 'jugador 3'), ('jugador 4', 'jugador 4')], max_length=20)),
                ('cartas', models.CharField(blank=True, max_length=20, null=True)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='partida.partida')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carta_des', models.CharField(max_length=20)),
                ('carta_mod', models.CharField(max_length=20)),
                ('carta_err', models.CharField(max_length=20)),
                ('carta_correcta', models.PositiveIntegerField(blank=True, null=True)),
                ('respuesta_jugador_1', models.PositiveIntegerField(blank=True, null=True)),
                ('respuesta_jugador_2', models.PositiveIntegerField(blank=True, null=True)),
                ('respuesta_jugador_3', models.PositiveIntegerField(blank=True, null=True)),
                ('jugador_pregunta', models.PositiveIntegerField()),
                ('jugador_responde', models.PositiveIntegerField()),
                ('tipo', models.CharField(choices=[('preguntar', 'preguntar'), ('acusar', 'acusar')], max_length=20)),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='partida.registro')),
            ],
        ),
        migrations.CreateModel(
            name='Tablero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carta_des_1', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_des_2', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_des_3', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_des_4', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_des_5', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_des_6', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_des_7', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_mod_1', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_mod_2', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_mod_3', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_mod_4', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_mod_5', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_mod_6', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_err_1', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_err_2', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_err_3', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_err_4', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_err_5', models.CharField(blank=True, max_length=50, null=True)),
                ('carta_err_6', models.CharField(blank=True, max_length=50, null=True)),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='partida.registro')),
            ],
        ),
    ]
