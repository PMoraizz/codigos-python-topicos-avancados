from django.shortcuts import render, redirect

prod1 = {
    'id': 1, 
    'nome': 'Computador', 
    'preco': 4510.80, 
    'resumo': 'Computador de última geração', 
    'descricao': 'Computador com processador Intel i7, 16GB de RAM, SSD de 512GB e placa de vídeo dedicada.'
}

prod2 = {
    'id': 2, 
    'nome': 'Celular', 
    'preco': 4520.00, 
    'resumo': 'Celular com câmera de alta resolução', 
    'descricao': 'Celular com câmera de 108MP, 128GB de armazenamento, bateria de longa duração e tela AMOLED.'
}

prod3 = {
    'id': 3, 
    'nome': 'Microondas', 
    'preco': 1530.00, 
    'resumo': 'Microondas com função grill', 
    'descricao': 'Microondas com capacidade de 30 litros, função grill, painel digital e 10 níveis de potência.'
}

prod4 = {
    'id': 4, 
    'nome': 'Geladeira', 
    'preco': 2500.00, 
    'resumo': 'Geladeira com tecnologia inverter', 
    'descricao': 'Geladeira com capacidade de 450 litros, tecnologia inverter, dispenser de água e prateleiras ajustáveis.'
}

prod5 = {
    'id': 5, 
    'nome': 'Televisão', 
    'preco': 3200.00, 
    'resumo': 'Televisão 4K com Smart TV', 
    'descricao': 'Televisão de 55 polegadas, resolução 4K, Smart TV com acesso a aplicativos e controle por voz.',
    'promocao': 'sim',
}

produtos = [ prod1, prod2, prod3, prod4, prod5 ]

# Create your views here.
def principal(request):
    contexto = {
        'quantidade': len(produtos),
        'produtos': produtos,
    }
    
    # contexto = {
    #     'quantidade': 0,
    #     'produtos': [],
    # }

    return render(request, 'produtos/lista_produtos.html', contexto)


def produto(request, id):

    if request.method == 'GET':
        produto = next((p for p in produtos if p['id'] == id), None)
        print(produto)
    
        contexto = { 'produto': produto }
        return render(request, 'produtos/detalhe_produto.html', contexto)
    else:
        return redirect('produtos:principal')