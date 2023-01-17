from django.shortcuts import render
from .models import Alunos

def index(request):
    alunos = {
        1:'Marcio',
        2:'Haiko',
        3:'Larissa'
    }
    dados = {
        'nome_do_aluno':alunos
    }
    return render(request, 'index.html', dados)

def aluno(request):
    alunos = {
        1:Alunos
    }
    dados = {
        'aluno' : alunos
    }
    return render(request, 'aluno.html', dados)