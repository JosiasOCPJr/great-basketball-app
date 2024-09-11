from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):  # Herda de AbstractUser para utilizar o sistema de autenticação do Django
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('Outro', 'Outro')], blank=True)

    class meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    # Aqui estamos definindo um related_name único para os grupos e permissões
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='hoops_app_usuario_set',
        blank=True,
        help_text='Os grupos aos quais este usuário pertence.',
        verbose_name='grupos'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='hoops_app_usuario_permissions_set',
        blank=True,
        help_text='Permissões específicas para este usuário.',
        verbose_name='permissões do usuário'
    )
    
    def __str__(self):
        return self.username
        

class Time():
    pass
