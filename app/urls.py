from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from sharepython.views import lobby_view, resumo_view, nova_tarefa_view, cadastrar_item_view, editar_tarefa_view, excluir_tarefa_view, atividades_view, cadastrar_atividade_view, editar_atividade_view, excluir_atividade_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lobby/', lobby_view, name='lobby'),
    path('resumo/', resumo_view, name='resumo'),
    path('novatarefa/', nova_tarefa_view, name='nova_tarefa'),
    path('cadastrar/', cadastrar_item_view, name='cadastrar_item'),
    path('atividades/', atividades_view, name='atividades'), 
    path('cadastrar_atividade/', cadastrar_atividade_view, name='cadastrar_atividade'),
    path('editar_tarefa/<int:item_id>/', editar_tarefa_view, name='editar_tarefa'),
    path('excluir_tarefa/<int:item_id>/', excluir_tarefa_view, name='excluir_tarefa'),
    path('editar_atividade/<int:atividade_id>/', editar_atividade_view, name='editar_atividade'),
    path('excluir_atividade/<int:atividade_id>/', excluir_atividade_view, name='excluir_atividade'),
]