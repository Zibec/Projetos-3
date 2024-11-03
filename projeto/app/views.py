from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Aluno, Simulado, Nota

def home(request):
    return render(request, 'home.html');

def cadastrar_notas(request, simulado_id):
    simulado = get_object_or_404(Simulado, id=simulado_id)
    alunos = simulado.alunos.all()

    if request.method == "POST":
        for aluno in alunos:
            nota_portugues = request.POST.get(f"nota_portugues_{aluno.id}")
            nota_matematica = request.POST.get(f"nota_matematica_{aluno.id}")

            # Armazenar ou atualizar notas
            nota, created = Nota.objects.update_or_create(
                aluno=aluno,
                simulado=simulado,
                defaults={
                    'nota_portugues': nota_portugues,
                    'nota_matematica': nota_matematica,
                }
            )

        return render(request, 'cadastrar_notas.html', {'alunos': alunos, 'success': True, 'simulado': simulado})

    return render(request, 'cadastrar_notas.html', {'alunos': alunos, 'simulado': simulado})

def cadastrar_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        sexo = request.POST.get('sexo')
        
        alunos = []
        alunos.append({
            'aluno': str(nome),
            'sexo': str(sexo),
            'idade': idade,
        })
        return HttpResponse("Aluno cadastrado!")
    
    return render(request, 'aluno.html')

def cadastrar_turma(request):
    if request.method == 'POST':
        nome_turma = request.POST.get('nome_turma')
        
        turmas = []
        turmas.append({
            'turma': str(nome_turma),
        })
        return HttpResponse("Turma cadastrada!")
    
    return render(request, 'turma.html')
        
