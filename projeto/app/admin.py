from django.contrib import admin
from .models import Aluno, Simulado, Nota, Professor, Pai

from django.contrib import admin
from .models import Aluno, Simulado, Nota, Professor, Turma, Pai, Tema

# Customização do admin para Aluno
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_de_nascimento', 'sexo', 'turma')

# Customização do admin para Simulado
class SimuladoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'peso_matematica', 'peso_portugues')

class NotaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'simulado', 'nota_portugues', 'nota_matematica')

# Customização do admin para Professor
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id',)  # Adicione outros campos se necessárior


# Customização do admin para Turma
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome_turma',)
    search_fields = ('nome_turma',)
    ordering = ('nome_turma',)


# Customização do admin para Pai
class PaiAdmin(admin.ModelAdmin):
    list_display = ('id','user',)
    search_fields = ('user__username',)
    filter_horizontal = ('alunos',)


# Customização do admin para Tema
class TemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'questoes_dificeis', 'questoes_faceis')
    search_fields = ('nome',)
    ordering = ('nome',)

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Simulado, SimuladoAdmin)
admin.site.register(Nota, NotaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Pai, PaiAdmin)
admin.site.register(Tema, TemaAdmin)