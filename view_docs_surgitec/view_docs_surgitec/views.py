from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Funcionario
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, 'home.html') 


def cadastrar_funcionario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        usuario = request.POST['usuario']
        senha = make_password(request.POST['senha'])
        funcao = request.POST['funcao']

        # Cria o usuário do Django
        user = User.objects.create(username=usuario, password=senha)

        # Cria o funcionário associado
        Funcionario.objects.create(nome=nome, usuario=user, funcao=funcao)

        return redirect('cadastrar_funcionario_sucesso')  # Redireciona para a página de sucesso

    return render(request, 'cadastrar_funcionario.html')

def cadastro_sucesso(request):
    return HttpResponse("Cadastro realizado com sucesso!")
