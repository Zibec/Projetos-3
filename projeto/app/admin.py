from django.contrib import admin
from .models import Aluno, Simulado, Nota, Professor, Pai

admin.site.register(Aluno)
admin.site.register(Simulado)
admin.site.register(Nota)
admin.site.register(Professor)
# Register your models here.