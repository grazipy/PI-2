
#definição das rotas de um app
#ligando as URLs às views que processarão as requisições e 
#organizando a navegação da aplicação

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'), #página de cadastro de funcionário
    path('cadastrar_funcionario/sucesso/', views.cadastro_sucesso, name='cadastrar_funcionario_sucesso'),  # funcionário cadastrado
    path('login/', views.login_view, name='login'), #pagina de login
    path('pagina_inicial/', views.pagina_inicial, name='pagina_inicial'),  # Página inicial pós-login
]



