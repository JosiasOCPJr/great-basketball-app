from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'html/tela_login/login2.html')

def cadastro(request):
    return render(request, 'html/cadastro/cadastro.html')

def forgot_pass(request):
    return render(request, 'html/esqueceu_a_senha/senha.html')

def main(request):
    return render(request, 'html/tela_principal/inicial.html')