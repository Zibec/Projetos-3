from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aluno, Simulado, Nota, Pai, Professor, Turma
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Página inicial para o pai
@login_required
def homePai(request):
    user = request.user
    print(user)
    return render(request, 'home_pai.html')


# Cadastro de notas de alunos em um simulado
def cadastrar_notas(request, simulado_id):
    simulado = get_object_or_404(Simulado, id=simulado_id)
    alunos = simulado.alunos.all()

    if request.method == "POST":
        for aluno in alunos:
            nota_portugues = request.POST.get(f"nota_portugues_{aluno.id}")
            nota_matematica = request.POST.get(f"nota_matematica_{aluno.id}")

            # Atualizar ou criar as notas no banco de dados
            Nota.objects.update_or_create(
                aluno=aluno,
                simulado=simulado,
                defaults={
                    'nota_portugues': float(nota_portugues) if nota_portugues else None,
                    'nota_matematica': float(nota_matematica) if nota_matematica else None,
                }
            )

        return render(request, 'cadastrar_notas.html', {'alunos': alunos, 'success': True, 'simulado': simulado})

    return render(request, 'cadastrar_notas.html', {'alunos': alunos, 'simulado': simulado})


# Cadastro de alunos
def cadastrar_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_de_nascimento = request.POST.get('data_de_nascimento')
        sexo = request.POST.get('sexo')
        turma_id = request.POST.get('turma_id')

        # Validar se a turma existe
        turma = get_object_or_404(Turma, id=turma_id)

        # Criar o aluno no banco de dados
        Aluno.objects.create(
            nome=nome,
            data_de_nascimento=data_de_nascimento,
            sexo=sexo,
            turma=turma
        )

        return HttpResponse("Aluno cadastrado com sucesso!")

    turmas = Turma.objects.all()  # Listar as turmas disponíveis para o formulário
    return render(request, 'cadastrar_aluno.html', {'turmas': turmas})


# Cadastro de turmas
def cadastrar_turma(request):
    if request.method == 'POST':
        nome_turma = request.POST.get('nome_turma')

        # Criar a turma no banco de dados
        Turma.objects.create(nome_turma=nome_turma)

        return HttpResponse("Turma cadastrada com sucesso!")

    return render(request, 'cadastrar_turma.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        if 'professor' in request.POST:
            return redirect('login_professor')
        elif 'pai' in request.POST:
            return redirect('login_pai')

# Login do Pai
def loginPai(request):
    if request.method == 'GET':
        return render(request, 'login_pai.html')

    elif request.method == 'POST':
        if 'entrar' in request.POST:
            nome = request.POST.get('nome')
            senha = request.POST.get('senha')
            user = authenticate(request, username=nome, password=senha)
            if user is not None:
                login(request, user)
                return redirect('home_pai')
            else:
                print("ERRO BURRO OTARIO")
                return render(request, 'login_pai.html', {'error': 'Credenciais inválidas'})


# Login do Professor
def loginProfessor(request):
    if request.method == 'GET':
        return render(request, 'login_professor.html')

    elif request.method == 'POST':
        if 'entrar' in request.POST:
            nome = request.POST.get('nome')
            senha = request.POST.get('senha')
            user = authenticate(request, username=nome, password=senha)
            if user is not None:
                login(request, user)
                return redirect('home_professor')  # Substituir pelo caminho correto da home do professor
            else:
                return render(request, 'login_professor.html', {'error': 'Credenciais inválidas'})

# Página inicial do professor
def homeProfessor(request):
    return render(request, 'home_professor.html')

