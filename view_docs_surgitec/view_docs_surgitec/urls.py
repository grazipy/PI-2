from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Atualizado para usar a função home do views.py
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('cadastrar_funcionario/sucesso/', views.cadastro_sucesso, name='cadastrar_funcionario_sucesso'),  # Nova URL
]



