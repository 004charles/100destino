from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128) 
    

class Companhia(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    senha = models.CharField(max_length=40)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# Classe Transportadora
class Transportadora(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Classe Viagem
class Viagem(models.Model):
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE, related_name='viagens')
    foto = models.ImageField(upload_to='viagens/', blank=True, null=True)  # Campo para foto da viagem ou passagem
    origem = models.CharField(max_length=100)  # Província de origem
    destino = models.CharField(max_length=100)  # Província de destino
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço da viagem
    data_partida = models.DateTimeField()  # Data e hora de partida
    data_chegada = models.DateTimeField()  # Data e hora de chegada

    def __str__(self):
        return f'{self.origem} para {self.destino} - {self.transportadora.nome}'

# Classe HorarioDisponivel para armazenar os horários específicos de uma viagem
class HorarioDisponivel(models.Model):
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE, related_name='horarios_disponiveis')
    horario = models.DateTimeField()  # Horário específico de uma viagem

    def __str__(self):
        return f'Horário: {self.horario} para {self.viagem}'

# Classe Rota
class Rota(models.Model):
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE, related_name='rotas')
    parada = models.CharField(max_length=255)  # Nome da parada
    horario_chegada = models.DateTimeField()  # Horário previsto de chegada na parada

    def __str__(self):
        return f'Rota {self.parada} para {self.viagem.origem} - {self.viagem.destino}'

# Classe Bilhete
class Bilhete(models.Model):
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE, related_name='bilhetes')
    nome_passageiro = models.CharField(max_length=100)  # Nome do passageiro
    documento_identificacao = models.CharField(max_length=50)  # Número do documento de identificação
    assento = models.CharField(max_length=5)  # Número do assento
    preco_pago = models.DecimalField(max_digits=10, decimal_places=2)  # Preço pago pelo bilhete
    data_compra = models.DateTimeField(auto_now_add=True)  # Data e hora da compra do bilhete
    status = models.CharField(max_length=20, choices=[('reservado', 'Reservado'), ('comprado', 'Comprado')])

    def __str__(self):
        return f'Bilhete {self.id} - {self.nome_passageiro} - {self.viagem}'
