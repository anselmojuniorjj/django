from django.urls import path
from .views import listagem, incluir, alterar, excluir

urlpatterns = [
    path('', listagem, name="url_listagem"),
    path('incluir/', incluir, name="url_incluir"),
    path('alterar/<int:pk>/', alterar, name="url_alterar"),
    path('excluir/<int:pk>/', excluir, name="url_excluir"),
]