from django.shortcuts import render
from django.http import HttpResponse

# Simulação de um banco de dados em memória
notas = []

def home(request):
    return render(request, 'home.html');

def cadastrar_nota(request):
    if request.method == 'POST':
        nome_aluno     = request.POST.get('nome_aluno')
        nota_portugues = request.POST.get('nota_portugues')
        nota_matematica = request.POST.get('nota_matematica')
        
        notas.append({
            'aluno'    : str(nome_aluno),
            'portugues': float(nota_portugues),
            'matematica': float(nota_matematica),
        })

        return HttpResponse("Notas cadastradas com sucesso!")

    return render(request, 'cadastrar_notas.html')
