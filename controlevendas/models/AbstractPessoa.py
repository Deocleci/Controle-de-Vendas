from django.db import models


class AbstractPessoa(models.Model):
    nome = models.CharField('Nome Completo', max_length=255)
    cpf = models.CharField('CPF', max_length=11, null=False, unique=True)
    dataNascimento = models.DateField('Data de nascimento')

    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)
    dataUltimaAlteracao = models.DateTimeField('Última alteração', null=True, blank=True, auto_now=True)

    class Meta:
        abstract = True
