from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('forgot_pass/', views.forgot_pass, name='esqueceu senha'),
    path('main/', views.main, name='main'),
]