from django.shortcuts import render, redirect
from django.contrib import messages
from loja.models import Cliente
from django.contrib.auth.models import User
from django.urls import reverse

def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_usuario')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        tel_celular = request.POST.get('tel_celular')
        senha = request.POST.get('senha')
        confirm_senha = request.POST.get('confirm_senha')

        if nome and email and senha and cpf and tel_celular and confirm_senha:
            if senha == confirm_senha:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'E-mail já cadastrado')
                elif Cliente.objects.filter(CPF=cpf).exists():
                    messages.error(request, 'CPF já cadastrado')
                elif Cliente.objects.filter(Telefone_celular=tel_celular).exists():
                    messages.error(request, 'Telefone celular já cadastrado')
                else:
                    user = User.objects.create_user(username=nome, email=email, password=senha)
                    user.save()
                    Cliente.objects.create(
                        user=user,
                        Nome=nome,
                        CPF=cpf,
                        Telefone_celular=tel_celular,
                    )
                    messages.success(request, 'Cadastro realizado com sucesso')
            else:
                messages.error(request, 'As senhas não estão iguais')
        else:
            messages.error(request, 'Preencha todos os campos')

    return render(request, template_name='cadastro.html', status=200)