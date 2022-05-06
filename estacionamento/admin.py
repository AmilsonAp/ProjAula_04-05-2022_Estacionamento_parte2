from django.contrib import admin
from estacionamento.models import Carro, Cliente, Funcionario, Fornecedo, Seguranca, Vagas, Locacao
# Register your models here.

admin.site.register(Carro)
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Fornecedo)
admin.site.register(Seguranca)
admin.site.register(Vagas)
admin.site.register(Locacao)

