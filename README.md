# Guia Completo: Criação e Configuração de um Projeto Django com Rotas, Views e Templates

Este `README.md` detalha os passos essenciais para iniciar e configurar um projeto Django, incluindo a criação de aplicações, definição de rotas, views, templates, e integração de CSS e Bootstrap. É baseado nos conceitos de Tópicos Avançados em Sistemas de Informação II - Desenvolvimento Web com Django.

---

## Sumário

1.  [Preparação do Ambiente](#1-preparação-do-ambiente)
2.  [Criação do Projeto Django](#2-criação-do-projeto-django)
3.  [Iniciar o Servidor de Desenvolvimento](#3-iniciar-o-servidor-de-desenvolvimento)
4.  [Criação de uma Aplicação Django](#4-criação-de-uma-aplicação-django)
5.  [Registrar a Aplicação no Projeto](#5-registrar-a-aplicação-no-projeto)
6.  [Configuração de Rotas (URLs)](#6-configuração-de-rotas-urls)
    * [urls.py da Aplicação](#urls.py-da-aplicação)
    * [urls.py do Projeto](#urls.py-do-projeto)
7.  [Criar a Primeira View (Funcionalidade)](#7-criar-a-primeira-view-funcionalidade)
8.  [Trabalhando com Templates (HTML Dinâmico)](#8-trabalhando-com-templates-html-dinâmico)
9.  [Usando Variáveis em Templates](#9-usando-variáveis-em-templates)
10. [Utilizando Filtros em Templates](#10-utilizando-filtros-em-templates)
11. [Herança de Templates](#11-herança-de-templates)
12. [Incluindo CSS e Bootstrap](#12-incluindo-css-e-bootstrap)
    * [CSS Personalizado](#css-personalizado)
    * [Bootstrap com django-bootstrap-v5](#bootstrap-com-django-bootstrap-v5-online)

---

## 1. Preparação do Ambiente

Antes de iniciar, certifique-se de que o **Python** e o **Django** estão instalados corretamente.

**Verificar Instalação do Python:**

    python --version

_(Exemplo de saída: Python 3.11.2)_

**Verificar Instalação do Django:**

    python -m pip list

***Procure por Django na lista. Se não estiver instalado, utilize:***

    python -m pip install django

## 2. Criação do Projeto Django
Organize seus projetos e crie um novo projeto Django.

**Crie a pasta principal para seus projetos (ex: Projetos):**

    mkdir Projetos
    cd Projetos 

**Crie o novo projeto Django (ex: MeuNovoProjeto):**

    django-admin startproject MeuNovoProjeto

_Regras: O nome do projeto não pode começar com número, conter acentuação ou espaços em branco._

**Estrutura gerada:**

    Projetos/
    └── MeuNovoProjeto/
        ├── MeuNovoProjeto/ (pasta interna com configurações do projeto)
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py

# 3. Iniciar o Servidor de Desenvolvimento
Verifique a instalação do projeto executando o servidor.

**Acesse a pasta raiz do seu projeto (onde está manage.py):**

    cd MeuNovoProjeto

**Inicie o servidor de desenvolvimento:**

    python manage.py runserver

# 4. Criação de uma Aplicação Django
Divida a funcionalidade do seu projeto em aplicações.

**Certifique-se de estar na pasta raiz do seu projeto (onde está manage.py):**

    cd Projetos/MeuNovoProjeto/

**Crie uma nova aplicação (ex: minha_app):**

    python manage.py startapp minha_app

**Estrutura gerada para a aplicação:**

    MeuNovoProjeto/
    ├── MeuNovoProjeto/
    └── minha_app/
        ├── migrations/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        └── views.py
    └── manage.py

# 5. Registrar a Aplicação no Projeto
Registre a nova aplicação nas configurações do projeto para que o Django a reconheça.

Abra `MeuNovoProjeto/MeuNovoProjeto/settings.py.`

Localize a lista `INSTALLED_APPS` e adicione o nome da sua aplicação:

    # MeuNovoProjeto/MeuNovoProjeto/settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'minha_app', # Adicione esta linha
    ]

# 6. Configuração de Rotas (URLs)
Defina os caminhos que o usuário acessará, organizando as URLs em níveis de projeto e aplicação.

## urls.py da Aplicação

Crie o arquivo `urls.py` dentro da pasta `minha_app/`:

    MeuNovoProjeto/
    ├── MeuNovoProjeto/
    └── minha_app/
        ├── ...
        └── urls.py  <-- Crie este arquivo
        └── views.py
    └── manage.py

Adicione o seguinte código a `minha_app/urls.py`

    # minha_app/urls.py
    from django.urls import path
    from . import views

    # Define o namespace para a aplicação (importante para evitar conflitos)
    app_name = 'minha_app' 

    urlpatterns = [
        path('', views.index, name='index'), # Rota para a função 'index' na views.py
        # Exemplo de rota com passagem de valores pela URL:
        path('detalhe/<int:id_item>/', views.detalhe_item, name='detalhe_item'),
        # Exemplo de rota com parâmetros via Query String (não precisa de configuração especial aqui):
        # path('pesquisa/', views.pesquisa, name='pesquisa'),
    ]

## urls.py do Projeto


Abra o arquivo `MeuNovoProjeto/MeuNovoProjeto/urls.py`.

Inclua as URLs da sua aplicação:

    # MeuNovoProjeto/MeuNovoProjeto/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('minha-app/', include('minha_app.urls')), # Inclui as URLs da sua aplicação
    ]

Isso significa que todas as URLs que começarem com `minha-app/` serão direcionadas para o arquivo `urls.py` da sua aplicação `minha_app`.

# 7. Criar a Primeira View (Funcionalidade)
Views são funções Python que processam requisições e retornam respostas.

Abra o arquivo `minha_app/views.py`.

Adicione o seguinte código:

    # minha_app/views.py
    from django.http import HttpResponse
    from django.shortcuts import render # Necessário para renderizar templates
    from django.shortcuts import redirect # Necessário para redirecionamentos
    import json # Para respostas JSON

    # View simples que retorna uma mensagem de texto
    def index(request):
        return HttpResponse("Hello World, Django !!!")

    # Exemplo de view com passagem de valores pela URL
    def detalhe_item(request, id_item):
        return HttpResponse(f"Detalhe do item ID: {id_item}")

    # Exemplo de view para processar parâmetros via Query String (GET)
    def pesquisa(request):
        query = request.GET.get('q', 'Nenhum termo de pesquisa') # .get() com valor padrão
        return HttpResponse(f"Resultados da pesquisa para: {query}")

    # Exemplo de view que retorna JSON (para APIs)
    def api_info(request):
        data = {
            "nome_app": "Minha Aplicação",
            "versao": "1.0",
            "servicos": [
                {"nome": "Index", "url": "/minha-app/"},
                {"nome": "Detalhe de Item", "url": "/minha-app/detalhe/<id>/"},
                {"nome": "Pesquisa", "url": "/minha-app/pesquisa/?q=<termo>"},
            ]
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

_Teste as rotas no navegador:_

**Inicie o servidor (python manage.py runserver) e teste:**

_http://127.0.0.1:8000/minha-app/ (para a index original)_

_http://127.0.0.1:8000/minha-app/detalhe/123/_

_http://127.0.0.1:8000/minha-app/pesquisa/?q=exemplo_

# 8. Trabalhando com Templates (HTML Dinâmico)
Use templates para gerar interfaces HTML com conteúdo dinâmico.

**Crie a estrutura de pastas para os templates:**

    MeuNovoProjeto/
    └── minha_app/
        └── templates/
            └── minha_app/  <-- Crie estas pastas
                └── index.html
                └── detalhe.html

**Crie o arquivo `minha_app/templates/minha_app/index.html`:**

    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Minha Aplicação Django</title>
    </head>
    <body>
        <h1>Bem-vindo à Minha Aplicação Django!</h1>
        <p>Esta é a página inicial.</p>
    </body>
    </html>

**Modifique a view para renderizar o template:**

    # minha_app/views.py
    from django.shortcuts import render

    def index(request):
        return render(request, 'minha_app/index.html')

# 9. Usando Variáveis em Templates
Passe dados da view para o template usando um dicionário de contexto.

**Modifique a view para passar um contexto:**

    # minha_app/views.py
    from django.shortcuts import render

    def index(request):
        contexto = {
            'titulo_pagina': 'Página Inicial Dinâmica',
            'nome_usuario': 'Mundo Django',
            'lista_itens': ['Item A', 'Item B', 'Item C']
        }
        return render(request, 'minha_app/index.html', contexto)

**Modifique o `index.html` para exibir as variáveis:**

    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>{{ titulo_pagina }}</title> {# Acessa a variável 'titulo_pagina' #}
    </head>
    <body>
        <h1>Bem-vindo, {{ nome_usuario }}!</h1> {# Acessa a variável 'nome_usuario' #}
        <h2>Lista de Itens:</h2>
        <ul>
            {% for item in lista_itens %} {# Tag for para iterar sobre a lista #}
                <li>{{ item }}</li>
            {% empty %} {# Bloco empty é renderizado se a lista estiver vazia #}
                <li>Nenhum item disponível.</li>
            {% endfor %}
        </ul>
        <p>Dados gerados no dia: {% now "d/m/Y" %}, às {% now "H:i:s" %}</p>
    </body>
    </html>

# 10. Utilizando Filtros em Templates
Filtros aplicam transformações aos valores das variáveis.

**Configuração de Idioma e Fuso Horário (`settings.py`): Essencial para formatação de data/hora e números.**

    # MeuNovoProjeto/MeuNovoProjeto/settings.py
    LANGUAGE_CODE = 'pt-br'       # Para formatação de números e datas em português
    TIME_ZONE = 'America/Sao_Paulo' # Ajuste conforme seu fuso horário
    USE_I18N = True               # Habilita internacionalização
    USE_TZ = True                 # Habilita fuso horário

Exemplos de uso de filtros (`minha_app/templates/minha_app/detalhe.html`):
**Modifique a view `detalhe_item` para passar um produto:**

    # minha_app/views.py
    def detalhe_item(request, id_item):
        produto_exemplo = {
            'id': id_item,
            'nome': 'computador gamer',
            'preco': 4510.80,
            'resumo': 'Computador com processador Intel i7, 16GB de RAM, SSD de 512GB.',
            'descricao': 'Computador com processador Intel i7, 16GB de RAM, SSD de 512GB e placa de vídeo RTX 3060 para a melhor experiência em jogos.',
            'promocao': True
        }
        # Filtro para encontrar o produto (simulado, em um projeto real viria do DB)
        produto_encontrado = produto_exemplo if produto_exemplo['id'] == id_item else None

        if request.method == 'POST':
            # Lógica para "simular compra" ou redirecionar
            return redirect('minha_app:index') # Redireciona para a página principal
        else: # GET
            contexto = {
                'produto': produto_encontrado,
                'qtd_produtos': 1 # Exemplo para pluralize
            }
            return render(request, 'minha_app/detalhe.html', contexto)

**Crie `minha_app/templates/minha_app/detalhe.html`:**

    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Detalhes do Produto</title>
    </head>
    <body>
        <h1>Detalhes do Produto:</h1>
        {% if produto %}
            <h2>{{ produto.nome|capfirst }}</h2> {# capfirst: primeira letra maiúscula #}
            <p>Preço: R$ {{ produto.preco|floatformat:"2g" }}</p> {# floatformat:"2g": 2 casas decimais, separador de milhar #}
            <p>Promoção: {{ produto.promocao|default:"indisponível" }}</p> {# default: valor padrão se vazio #}
            {% if produto.promocao %}
                <p>Desconto: 10%</p>
            {% endif %}
            <p>Resumo: {{ produto.resumo|truncatechars:50 }}</p> {# truncatechars: limita caracteres #}
            <p>Descrição: {{ produto.descricao|truncatewords:15 }}</p> {# truncatewords: limita palavras #}
            <p>Temos {{ qtd_produtos }} produto{{ qtd_produtos|pluralize:"s" }} disponível{{ qtd_produtos|pluralize:"l,is" }}.</p> {# pluralize: adiciona plural #}

            <form action="{% url 'minha_app:detalhe_item' produto.id %}" method="post">
                {% csrf_token %} {# Tag de segurança obrigatória em formulários POST #}
                <label for="quantidade">Quantidade:</label>
                <input type="number" id="quantidade" name="quantidade" value="1" min="1">
                <button type="submit">Simular Compra</button>
            </form>
            <p><a href="{% url 'minha_app:index' %}">Voltar para a lista</a></p>
        {% else %}
            <p>Produto não encontrado.</p>
        {% endif %}
    </body>
    </html>

# 11. Herança de Templates
Reaproveite estruturas HTML comuns entre suas páginas.

Crie um template base (`minha_app/templates/base.html`):

**Crie o arquivo diretamente em `minha_app/templates/`, não dentro da subpasta `minha_app/`.**

    MeuNovoProjeto/
    └── minha_app/
        └── templates/
            ├── base.html  <-- Crie este arquivo
            └── minha_app/
                └── index.html
                └── detalhe.html

**Conteúdo de `minha_app/templates/base.html`:**              

    {% load static %}
    {% load bootstrap5 %} {# Se estiver usando Bootstrap #}
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>{% block titulo_aba %}{% endblock %}</title> {# Bloco para o título da aba #}
        <link rel="stylesheet" href="{% static 'css/estilo.css' %}"> {# Seu CSS personalizado #}
        {% bootstrap_css %} {# Se estiver usando Bootstrap #}
    </head>
    <body>
        {% bootstrap_javascript %} {# Se estiver usando Bootstrap #}
        <div class="container"> {# Classe Bootstrap para centralizar o conteúdo #}
            <header>
                <h1>{% block titulo_pagina %}{% endblock %}</h1> {# Bloco para o título principal da página #}
                <h3>{% block subtitulo_pagina %}{% endblock %}</h3> {# Bloco para um subtítulo #}
                <p>Data atual: {% now "d/m/Y" %} | Hora: {% now "H:i" %}</p>
                <hr>
            </header>
            <main>
                {% block conteudo %}{% endblock %} {# Bloco para o conteúdo principal específico de cada página #}
            </main>
            <footer>
                <hr>
                <p>&copy; 2025 Meu Novo Projeto Django. Todos os direitos reservados.</p>
            </footer>
        </div>
    </body>
    </html>

Adapte seus templates (`index.html`, `detalhe.html`) para estenderem `base.html`:

**Exemplo para `minha_app/templates/minha_app/index.html`:**

    {% extends 'base.html' %} {# Deve ser a primeira linha #}

    {% block titulo_aba %}Página Principal de Produtos{% endblock %}
    {% block titulo_pagina %}Lista de Produtos{% endblock %}
    {% block subtitulo_pagina %}Confira todos os nossos itens!{% endblock %}

    {% block conteudo %}
        <p>Esta é a página principal que exibe a lista de produtos.</p>
        {# Adicione aqui a lógica de listagem de produtos com um loop for e links para detalhes #}
        <ul>
            {% for item in lista_itens %}
                <li>{{ item }} - <a href="{% url 'minha_app:detalhe_item' forloop.counter %}">Ver Detalhes</a></li>
            {% empty %}
                <li>Nenhum produto disponível no momento.</li>
            {% endfor %}
        </ul>
        <form action="" method="post">
            {% csrf_token %}
            <button type="submit" class="btn btn-primary">Atualizar Lista</button> {# Exemplo com classe Bootstrap #}
        </form>
    {% endblock %}

Faça o mesmo para `minha_app/templates/minha_app/detalhe.html`, ajustando os blocos conforme necessário.

# 12. Incluindo CSS e Bootstrap
Estilize sua aplicação com CSS personalizado e/ou o framework Bootstrap.

## CSS Personalizado

**Crie a pasta `static` e `css` dentro da sua aplicação:**

    MeuNovoProjeto/
    └── minha_app/
        └── static/
            └── css/  <-- Crie estas pastas
                └── estilo.css

**Adicione estilos em `minha_app/static/css/estilo.css` (exemplo):**

    /* minha_app/static/css/estilo.css */
    body {
        font-family: 'Inter', sans-serif; /* Usando Inter como recomendado */
        margin: 0;
        background-color: #e2e8f0; /* Um tom de cinza claro do Tailwind */
    }
    .container {
        padding: 1.25rem; /* p-5 do Tailwind */
        margin: 1.25rem auto; /* mx-auto my-5 do Tailwind */
        background-color: #ffffff; /* bg-white do Tailwind */
        border-radius: 0.5rem; /* rounded-lg do Tailwind */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1); /* shadow-md do Tailwind */
    }
    h1, h2, h3 {
        color: #1a202c; /* text-gray-900 do Tailwind */
        margin-bottom: 1rem; /* mb-4 do Tailwind */
    }
    a {
        color: #3b82f6; /* text-blue-500 do Tailwind */
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    button {
        background-color: #4299e1; /* bg-blue-500 do Tailwind */
        color: white;
        padding: 0.5rem 1rem; /* py-2 px-4 do Tailwind */
        border-radius: 0.375rem; /* rounded-md do Tailwind */
        border: none;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    button:hover {
        background-color: #3182ce; /* bg-blue-600 do Tailwind */
    }
    ul {
        list-style: disc; /* bullet points */
        padding-left: 1.25rem; /* pl-5 do Tailwind */
    }
    li {
        margin-bottom: 0.5rem; /* mb-2 do Tailwind */
    }

**Inclua o CSS no `base.html`:**

    {% load static %}
    <head>
        <link rel="stylesheet" href="{% static 'css/estilo.css' %}">
    </head>

## Bootstrap com django-bootstrap-v5 (Online)

Instale o pacote:

    pip install django-bootstrap-v5

**Adicione 'bootstrap5' em INSTALLED_APPS no settings.py:**

    # MeuNovoProjeto/MeuNovoProjeto/settings.py
    INSTALLED_APPS = [
        # ... outras apps
        'bootstrap5', # Adicione esta linha
        'minha_app',
    ]

**Carregue e inclua o Bootstrap no base.html:**

    {% load static %}
    {% load bootstrap5 %} {# Carrega a biblioteca de tags do Bootstrap #}
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        {% bootstrap_css %} {# Inclui o CSS do Bootstrap #}
        {# Opcional: Remova seu CSS personalizado se o Bootstrap for sobrescrevê-lo #}
        {# <link rel="stylesheet" href="{% static 'css/estilo.css' %}"> #}
    </head>
    <body>
        {% bootstrap_javascript %} {# Inclui o JS do Bootstrap #}
        <div class="container"> {# Utilize as classes Bootstrap, como 'container' #}
            </div>
    </body>
    </html>

