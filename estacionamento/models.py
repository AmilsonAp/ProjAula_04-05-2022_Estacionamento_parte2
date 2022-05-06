from django.db import models

# Create your models here.
class Carro(models.Model):
    placa = models.CharField(max_length=7)
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anoFabricacao = models.DateField()
    dataModelo = models.DateField()
    cor = models.CharField(max_length=20)

    def __str__(self):
        return self.placa
        return self.nome
        return self.marca
        return self.modelo
        return self.anoFabricacao
        return self.anoModelo
        return self.cor

class Cliente(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    nomePai = models.CharField(max_length=50)
    nomeMae = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.cpf
        return self.nome
        return self.telefone
        return self.endereco
        return self.cidade
        return self.nomePai
        return self.nomeMae
        return self.email

class Funcionario(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    salario = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.cpf
        return self.nome
        return self.salario
        return self.email
        return self.telefone
        return self.endereco
        return self.email

class Fornecedo(models.Model):
    cnpj = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.cnpj
        return self.nome
        return self.tipo
        return self.telefone
        return self.endereco
        return self.email

class Seguranca(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.cpf
        return self.nome
        return self.telefone
        return self.email

class Vagas(models.Model):
    _id = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self._id
        return setf.descricao

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    carro = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    dataLocacao = models.DateField()
    valor = models.CharField(max_length=10)
    dataDevolucao = models.DateField()

    def __str__(self):
        return self.dataLocacao + self.valor + self.dataDevolucao


