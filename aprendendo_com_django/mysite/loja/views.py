from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import categoria, produto
from django.http import Http404


def index(request):
    latest_categoria_list = categoria.objects.order_by('-pub_date')[:5]
    template = loader.get_template('loja/index.html')
    context = {"latest_categoria_list": latest_categoria_list}
    return HttpResponse(template.render(context, request))

def detalhe(request, produto_id):
    produto = get_object_or_404(pk = produto_id)
    return render(request, 'loja/detalhes.html', {'produto':produto})

def resultado(request, produto_id):
    resposta = 'vc está olhando o produto %s' % produto_id
    return HttpResponse(resultado % produto_id)

def preco(request, produto_id):
    return HttpResponse('vc adicionou %s ao seu carrinho' % produto_id)
