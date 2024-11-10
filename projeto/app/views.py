from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aluno, Simulado, Nota, Pai, Professor
from django.contrib.auth import authenticate, login

def homePai(request):
    return render(request, 'home_pai.html')

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
        
def loginPai(request):
    if request.method == 'GET':
        return render(request, 'login_pai.html')
    
    elif request.method == 'POST':
        if 'entrar' in request.POST:
            nome = request.POST.get('nome')
            senha = request.POST.get('senha')
            user = authenticate(request, username=nome, password=senha)
            if user.is_authenticated:
                login(request, user)
                return HttpResponseRedirect('/home_pai')
            else:
                return render(request, 'login_pai', {'error': 'Credenciais inválidas'})
            
        elif 'professor' in request.POST:
            return HttpResponseRedirect('/login_professor/')#deve retornar a pagina de login do professor quando ela existir
        
def loginProfessor(request):
    if request.method == 'GET':
        return render(request, 'login_pai')
    
    elif request.method == 'POST':
        if 'entrar' in request.POST:
            nome = request.POST.get('nome')
            senha = request.POST.get('senha')
            user = authenticate(request, username=nome, password=senha)
            if user.is_authenticated:
                return HttpResponseRedirect('home_professor/')
            else:
                return render(request, 'login_professor.html', {'error': 'Credenciais inválidas'})
            
        elif 'responsável' in request.POST:
            return HttpResponseRedirect('login_pai/')
            