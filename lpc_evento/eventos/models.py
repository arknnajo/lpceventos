from django.db import models
from django.contrib.auth.models import User

class Endereco (models.Model):
    logradouro = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256, null=True)
    uf= models.CharField(max_length=2, null=True)
    cidade = models.CharField(max_length=64, null=True)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return'{}-{},{}'.format(self.logradouro, self.cidade, self.uf)


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name = 'pessoas', null =True, blank= False)
    ususario = models.OneToOneField(User)

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length = 32)
    pai = models.CharField(max_length = 128)
    mae = models.CharField(max_length = 128)

    def __str__(self):
        return self.cpf

class Evento (models.Model):
    nome = models.CharField(max_length = 218)
    descricao = models.TextField()
    sigla = models.CharField(max_length=15)
    numero = models.IntegerField()
    ano = models.DateField(blank=True)
    realizador = models.ForeignKey(PessoaFisica, related_name = 'pessoafisicas', null=True, blank=False )
    endereco = models.ForeignKey(Endereco, related_name = 'pessoafisicas', null =True, blank= False)
    logo = models.CharField(max_length = 10)
    data_de_inicio = models.DateField(blank=True, null=True)
    data_de_fim = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.nome

class Inscricao (models.Model):
    evento = models.ForeignKey(Evento, related_name = 'evento', null=True, blank=False)
    pessoa = models.ForeignKey(PessoaFisica, related_name = 'pessoafisic', null=True, blank=False)
    data_de_inscricao = models.DateField(blank=True, null=True)
    preco = models.FloatField()
    def __str__(self):
        return self.evento
