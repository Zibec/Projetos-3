from django.db import models
from django.contrib.auth.models import User
from abc import ABC, abstractmethod


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE, related_name='alunos')

    def __str__(self):
        return self.nome


class Simulado(ABC, models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno, related_name='simulados')

    class Meta:
        abstract = True

    @abstractmethod
    def calcular_nota(self, aluno):
        pass

    def __str__(self):
        return self.nome


class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    simulado = models.ForeignKey('Simulado', on_delete=models.CASCADE)  
    nota_portugues = models.FloatField(null=True, blank=True)
    nota_matematica = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.simulado.nome}"


class Pai(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aluno = models.ManyToManyField(Aluno, related_name='pais')
    nomePai = models.CharField(max_length=100)

    def __str__(self):
        return self.nomePai


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomeProfessor = models.CharField(max_length=100)

    def cadastrar_aluno(self, aluno):
        pass

    def cadastrar_nota(self, simulado, aluno, nota):
        if not hasattr(simulado, 'notas'):
            simulado.notas = {}
        simulado.notas[aluno.id] = nota

    def editar_nota(self, simulado, aluno, nova_nota):
        pass

    def visualizar_aluno(self, aluno):
        pass

    def __str__(self):
        return self.nomeProfessor


class Turma(models.Model):
    nome_turma = models.CharField(max_length=100)
    simulados = models.ManyToManyField('Simulado', related_name='turmas')  
    professor = models.ManyToManyField(Professor, related_name='professor_turma')

    def ordenar_notas(self):
        pass

    def calcular_media(self):
        alunos = Aluno.objects.filter(turma=self)
        notas = Nota.objects.filter(aluno__in=alunos)
        if not notas.exists():
            return 0
        total_notas = sum(aluno.nota for aluno in alunos if aluno.nota is not None)
        num_alunos = notas.count()

        return total_notas / num_alunos if num_alunos > 0 else 0

    def __str__(self):
        return self.nome_turma


class ColegiosMilitares(Simulado):
    peso_matematica = models.FloatField()
    peso_portugues = models.FloatField()

    def calcular_nota(self, aluno):
        nota = Nota.objects.get(aluno=aluno, simulado=self)
        return (nota.nota_matematica * self.peso_matematica + nota.nota_portugues * self.peso_portugues) / (self.peso_matematica + self.peso_portugues)


class ColegioAplicacao(Simulado):
    peso = models.FloatField()
    media = models.FloatField()

    def calcular_nota(self, aluno):
        nota = Nota.objects.get(aluno=aluno, simulado=self)
        return (nota.nota_matematica + nota.nota_portugues) / 2
