from django.db import models
from django.contrib.auth.models import User

# Classe Professor
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor', default=None)

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

# Classe Simulado

class Simulado(models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField('Aluno', related_name='simulados')
    peso_matematica = models.FloatField()
    peso_portugues = models.FloatField()

    def calcular_nota(self, aluno):
        
        #Calcula a nota ponderada de um aluno no simulado.
        
        try:
            nota = Nota.objects.get(aluno=aluno, simulado=self)
            total_peso = self.peso_matematica + self.peso_portugues
            return (
                (nota.nota_matematica * self.peso_matematica) +
                (nota.nota_portugues * self.peso_portugues)
            ) / total_peso
        except Nota.DoesNotExist:
            return None

# Classe Turma
class Turma(models.Model):
    nome_turma = models.CharField(max_length=100)
    professor = models.ManyToManyField(Professor, related_name='turmas', null=True)
    simulados = models.ManyToManyField(Simulado, related_name='turmas', null=True, blank=True)

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


# Classe Aluno
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos')

# Classe Pai
class Pai(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pai')
    alunos = models.ManyToManyField(Aluno, related_name='pais')

# Classe Nota
class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    simulado = models.ForeignKey(Simulado, on_delete=models.CASCADE, null=True)
    nota_portugues = models.FloatField(null=True, blank=True)
    nota_matematica = models.FloatField(null=True, blank=True)


# Classe Tema
class Tema(models.Model):
    nome = models.CharField(max_length=100)
    questoes_dificeis = models.IntegerField()
    questoes_faceis = models.IntegerField()
    