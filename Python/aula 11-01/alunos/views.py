from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Alunos
from django.forms import ModelForm

class AlunosForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome_aluno', 'descricao_profissional', 'descricao_pessoal', 'habilidades', 'comportamento', 'workspace', 'categoria', 'date_aluno']

def index(request):
    aluno = Alunos.objects.all()
    alunos = {'alunos':aluno}
    return render(request, 'index.html', alunos)


def aluno(request, aluno_id):
    alunos = get_object_or_404(Alunos, pk=aluno_id)
    aluno_a_exibir = {'aluno':alunos}
    
    return render(request, 'aluno.html', aluno_a_exibir)
