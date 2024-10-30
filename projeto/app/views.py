from django.shortcuts import render
from django.http import HttpResponse


# Simulação de um banco de dados em memória
notas = []

def home(request):
    return render(request, 'home.html');

def cadastrar_nota(request):
    if request.method == 'POST':
        nome_aluno = request.POST.get('nome_aluno')
        nota_portugues = request.POST.get('nota_portugues')
        nota_matematica = request.POST.get('nota_matematica')
        
        notas.append({
            'aluno'    : str(nome_aluno),
            'portugues': float(nota_portugues),
            'matematica': float(nota_matematica),
        })

        return HttpResponse("Notas cadastradas com sucesso!")

    return render(request, 'cadastrar_notas.html')

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
        
