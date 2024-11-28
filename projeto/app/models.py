from django.db import models
from django.contrib.auth.models import User

    

class Pai(User):
    user_ptr=None
    nome_pai = models.CharField(max_length=100)
    alunos = models.ManyToManyField('Aluno', related_name='pais')
    
    def __str__(self):
        return self.nome_pai


#user_ptr

# Classe Professor
class Professor(User):
    user_ptr=None
    def cadastrar_nota(self, simulado, aluno, nota_portugues, nota_matematica):
        Nota.objects.create(
            aluno=aluno,
            simulado=simulado,
            nota_portugues=nota_portugues,
            nota_matematica=nota_matematica
        )

    def editar_nota(self, nota, nova_nota_portugues, nova_nota_matematica):
        nota.nota_portugues = nova_nota_portugues
        nota.nota_matematica = nova_nota_matematica
        nota.save()

    def visualizar_alunos(self, turma):
        return turma.alunos.all()

    def __str__(self):
        return self.nome


# Classe Aluno
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE, related_name='alunos', default=None)

    def __str__(self):
        return self.nome


# Classe Simulado
class Simulado(models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno, related_name='simulados')
    peso_matematica = models.FloatField(default=1.0)
    peso_portugues = models.FloatField(default=1.0)

    def calcular_nota(self, aluno):
        """
        Calcula a nota ponderada de um aluno no simulado.
        """
        try:
            nota = Nota.objects.get(aluno=aluno, simulado=self)
            total_peso = self.peso_matematica + self.peso_portugues
            return (
                (nota.nota_matematica * self.peso_matematica) +
                (nota.nota_portugues * self.peso_portugues)
            ) / total_peso
        except Nota.DoesNotExist:
            return None

    def __str__(self):
        return self.nome


# Classe Nota
class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    simulado = models.ForeignKey(Simulado, on_delete=models.CASCADE)
    nota_portugues = models.FloatField(null=True, blank=True)
    nota_matematica = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.simulado.nome}"


# Classe Tema
class Tema(models.Model):
    nome = models.CharField(max_length=100)
    questoes_dificeis = models.IntegerField()
    questoes_faceis = models.IntegerField()

    def __str__(self):
        return self.nome


# Classe Turma
class Turma(models.Model):
    nome_turma = models.CharField(max_length=100)
    professor = models.ManyToManyField(Professor, related_name='turmas')
    simulados = models.ManyToManyField(Simulado, related_name='turmas')

    def ordenar_notas(self):
        """
        Ordena os alunos da turma pelo nome.
        """
        return sorted(self.alunos.all(), key=lambda aluno: aluno.nome)

    def calcular_media(self):
        """
        Calcula a média geral das notas dos alunos da turma.
        """
        alunos = self.alunos.all()
        notas = Nota.objects.filter(aluno__in=alunos)
        total_notas = sum((nota.nota_portugues or 0) + (nota.nota_matematica or 0) for nota in notas)
        num_notas = notas.count() * 2  # Português e Matemática
        return total_notas / num_notas if num_notas > 0 else 0

    def __str__(self):
        return self.nome_turma
