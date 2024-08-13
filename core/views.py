from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    vnome = request.POST.get("nome")
    vidade = request.POST.get("idade")
    vtelefone = request.POST.get("telefone")
    vprofissao = request.POST.get("profissao")
    if vnome and vidade:  # Verifica se os campos não estão vazios
        Pessoa.objects.create(nome=vnome, idade=vidade, telefone=vtelefone, profissao=vprofissao)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        telefone = request.POST.get('telefone')
        profissao = request.POST.get('profissao')
        pessoa.nome = nome
        pessoa.idade = idade
        pessoa.telefone = telefone
        pessoa.profissao = profissao
        pessoa.save()
        return redirect('home')
    return render(request, 'editar.html', {'pessoa': pessoa})

def excluir(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('home')
    return render(request, 'excluir.html', {'pessoa': pessoa})
