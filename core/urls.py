from django.urls import path # type: ignore
from .views import home, salvar, editar, excluir

urlpatterns = [
    path('', home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>/', editar, name='editar'),
    path('excluir/<int:id>/', excluir, name='excluir'),
]

