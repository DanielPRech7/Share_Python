from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from sharepython.views import lobby_view
from sharepython.views import resumo_view
from sharepython.views import nova_tarefa_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lobby/', lobby_view, name='lobby'),
    path('resumo/', resumo_view, name='resumo'),
    path('novatarefa/', nova_tarefa_view, name='nova_tarefa'),
]
