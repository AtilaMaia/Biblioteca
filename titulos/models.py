from django.db import models

# Create your models here.
"""
Criando os campos necessarios para o controle de 
livros em uma biblioteca...

Títulos
->Título = STR*;
->Autor = STR*;
->Editora=STR*;
->Gênero=STR*;
->Ano da Publicação=DATETIME*;
->Descrição= TEXTO*;
->CAPA= IMG*.
->SITUAÇAO= SITUAÇÃO
-> Data_devoluçao= datatype

SITUAÇÃO
nome: str*


Cadastro de usuários da biblioteca:

nome: STR*
sobrenome: STR*
Email: str*
telefone: str*
cpf: str*
endereço: str*
statos: str*


"""
objects=models.Manager()

class Sit(models.Model):

    situ = models.CharField(max_length=15)

    def __str__(self):
        return self.situ


class Titulo(models.Model):

    livro = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    descricao = models.TextField(max_length=750, blank=True)
    pub = models.DateField()
    data_emprestimo = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    sit = models.ForeignKey(Sit, on_delete=models.DO_NOTHING)

    
    def __str__(self):
        return self.livro

# criar app USUARIO
