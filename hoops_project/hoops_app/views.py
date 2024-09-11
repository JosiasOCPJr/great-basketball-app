from django.shortcuts import render
from .forms import UsuarioForm
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'html/index/index.html')
def login(request):
    return render(request, 'html/tela_login/login2.html')

def cadastro_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autentica o usuário após o cadastro
            '''return redirect('profile')  # Redireciona para o perfil do usuário'''
    else:
        form = UsuarioForm()
    return render(request, 'hoops_app/cadastro.html', {'form': form})

def forgot_pass(request):
    return render(request, 'html/esqueceu_a_senha/senha.html')

def main(request):
    return render(request, 'html/tela_principal/inicial.html')