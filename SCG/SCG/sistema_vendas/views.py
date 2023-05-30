from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Cliente, Estoque

def pagina_inicial(request):
    return render(request, 'sistema_vendas/pagina_inicial.html')

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        documento_identidade = request.POST.get('documento_identidade')
        cpf = request.POST.get('cpf')

        cliente = Cliente.objects.create(nome=nome, documento_identidade=documento_identidade, cpf=cpf)
        cliente.save()

        return render(request, 'cadastrar_cliente.html', {'cliente': cliente})

    return render(request, 'cadastrar_cliente.html')


def entrada_estoque(request):
    if request.method == 'POST':
        nome_peca = request.POST.get('nome_peca')
        quantidade = int(request.POST.get('quantidade'))
        valor_unitario = float(request.POST.get('valor_unitario'))

        estoque = Estoque.objects.filter(nome_peca=nome_peca).first()
        if estoque:
            estoque.quantidade += quantidade
            estoque.valor_unitario = valor_unitario
        else:
            estoque = Estoque.objects.create(nome_peca=nome_peca, quantidade=quantidade, valor_unitario=valor_unitario)

        estoque.save()

        return render(request, 'entrada_estoque.html', {'estoque': estoque})

    return render(request, 'entrada_estoque.html')


def consultar_estoque(request):
    estoque = Estoque.objects.all()
    return render(request, 'consultar_estoque.html', {'estoque': estoque})


def realizar_venda(request):
    if request.method == 'POST':
        codigo_cliente = request.POST.get('codigo_cliente')
        quantidade = int(request.POST.get('quantidade'))
        nome_peca = request.POST.get('nome_peca')

        cliente = Cliente.objects.filter(codigo=codigo_cliente).first()
        estoque = Estoque.objects.filter(nome_peca=nome_peca).first()

        if not cliente:
            return render(request, 'realizar_venda.html', {'mensagem': 'Cliente não encontrado.'})

        if not estoque:
            return render(request, 'realizar_venda.html', {'mensagem': 'Peça não encontrada no estoque.'})

        if estoque.quantidade < quantidade:
            return render(request, 'realizar_venda.html', {'mensagem': 'Quantidade insuficiente no estoque.'})

        valor_unitario = estoque.valor_unitario
        valor_total = valor_unitario * quantidade

        estoque.quantidade -= quantidade
        estoque.save()

        return render(request, 'realizar_venda.html', {
            'cliente': cliente,
            'nome_peca': nome_peca,
            'quantidade': quantidade,
            'valor_unitario': valor_unitario,
            'valor_total': valor_total
        })

    return render(request, 'realizar_venda.html')