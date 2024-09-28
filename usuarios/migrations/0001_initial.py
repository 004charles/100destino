# Generated by Django 5.1.1 on 2024-09-28 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transportadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='viagens/')),
                ('origem', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_partida', models.DateTimeField()),
                ('data_chegada', models.DateTimeField()),
                ('transportadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viagens', to='usuarios.transportadora')),
            ],
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parada', models.CharField(max_length=255)),
                ('horario_chegada', models.DateTimeField()),
                ('viagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rotas', to='usuarios.viagem')),
            ],
        ),
        migrations.CreateModel(
            name='HorarioDisponivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('viagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios_disponiveis', to='usuarios.viagem')),
            ],
        ),
        migrations.CreateModel(
            name='Bilhete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_passageiro', models.CharField(max_length=100)),
                ('documento_identificacao', models.CharField(max_length=50)),
                ('assento', models.CharField(max_length=5)),
                ('preco_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_compra', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('reservado', 'Reservado'), ('comprado', 'Comprado')], max_length=20)),
                ('viagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bilhetes', to='usuarios.viagem')),
            ],
        ),
    ]
