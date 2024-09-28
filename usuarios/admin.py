from django.contrib import admin
from .models import Transportadora, Viagem, HorarioDisponivel, Rota, Bilhete

# Registro do modelo Transportadora
@admin.register(Transportadora)
class TransportadoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'endereco', 'data_criacao')
    search_fields = ('nome', 'email')
    list_filter = ('data_criacao',)

# Inline para HorariosDisponiveis na Viagem
class HorarioDisponivelInline(admin.TabularInline):
    model = HorarioDisponivel
    extra = 1  # Número de formulários extras para adicionar novos horários

# Registro do modelo Viagem com HorariosDisponiveisInline
@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = ('transportadora', 'origem', 'destino', 'preco', 'data_partida', 'data_chegada')
    search_fields = ('origem', 'destino', 'transportadora__nome')
    list_filter = ('data_partida', 'data_chegada', 'transportadora')
    inlines = [HorarioDisponivelInline]  # Adiciona os horários disponíveis na edição de Viagem

# Registro do modelo Rota
@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    list_display = ('viagem', 'parada', 'horario_chegada')
    search_fields = ('viagem__origem', 'viagem__destino', 'parada')
    list_filter = ('horario_chegada',)

# Registro do modelo Bilhete
@admin.register(Bilhete)
class BilheteAdmin(admin.ModelAdmin):
    list_display = ('viagem', 'nome_passageiro', 'documento_identificacao', 'assento', 'preco_pago', 'status', 'data_compra')
    search_fields = ('nome_passageiro', 'documento_identificacao', 'viagem__origem', 'viagem__destino')
    list_filter = ('status', 'data_compra', 'viagem')

# Registro direto de HorarioDisponivel (Opcional)
@admin.register(HorarioDisponivel)
class HorarioDisponivelAdmin(admin.ModelAdmin):
    list_display = ('viagem', 'horario')
    list_filter = ('horario', 'viagem__transportadora')
    search_fields = ('viagem__origem', 'viagem__destino')



from .models import Companhia 

class CompanhiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'data_criacao')  # Campos que você deseja exibir na lista
    search_fields = ('nome', 'email')  # Campos que você deseja usar para busca

admin.site.register(Companhia, CompanhiaAdmin)  # Registrar o modelo Companhia com a classe CompanhiaAdmin
