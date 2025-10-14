from django.urls import path
from . import views

app_name = 'loja'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:produto_id/>', views.detalhe, name='detalhes' ),
    path('<int:produto_id/resultado>', views.resultado, name='resultado'),
    path('<int:produto_id/preco>', views.preco, name='quantidade')
]