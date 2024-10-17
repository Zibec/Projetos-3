from django.db import models
from django.utils import timezone


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])

class Simulado(models.Model):
    nome_simulado = models.CharField(max_length=100)
    acertos_matematica = models.IntegerField()
    acertos_portugues = models.IntegerField()
    data_aplicacao = models.DateField(default=timezone.now)
    alunos = models.ManyToManyField(Aluno, related_name='simulados')

    def __str__(self):
        return self.nome_simulado
    
class Aluno(models.Model):
    simulados = models.ManyToManyField(Simulado, related_name='alunos')

    def __str__(self):
        return self.nome
    
class Pai(models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno, related_name='pais')

    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def cadastrar_nota(self, simulado, aluno, nota):
        # Lógica para cadastrar uma nota
        pass

    def editar_nota(self, simulado, aluno, nova_nota):
        # Lógica para editar a nota de um aluno
        pass

    def visualizar_aluno(self, aluno):
        # Lógica para visualizar informações do aluno
        pass

    def __str__(self):
        return self.nome
class Turma(models.Model):
    nome_turma = models.CharField(max_length=100)
    simulados = models.ManyToManyField(Simulado, related_name='turmas')

    def ordenar_notas(self):
        # Lógica para ordenar notas dos alunos
        pass

    def calcular_media(self):
        # Lógica para calcular a média das notas dos alunos
        pass

    def __str__(self):
        return self.nome_turma
class ColegioAplicacao(models.Model):
    peso_matematica = models.FloatField()
    peso_portugues = models.FloatField()

    def calcular_nota(self, simulado):
        # Lógica para calcular a nota usando pesos
        pass
class ColegioMilitar(models.Model):
    peso_matematica = models.FloatField()
    peso_portugues = models.FloatField()

    def calcular_nota(self, simulado):
        # Lógica para calcular a nota usando pesos específicos
        pass
class ColegioPoliciaMilitar(models.Model):
    peso = models.FloatField()
    media = models.FloatField()

    def calcular_nota(self, simulado):
        # Lógica para calcular a nota de acordo com o colégio policial militar
        pass
