from django.contrib import admin
from eventos.models import Pessoa
from eventos.models import Endereco
from eventos.models import PessoaFisica
from eventos.models import Evento
from eventos.models import Inscricao

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(Inscricao)
