from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        return HttpResponse(f"Cadastro realizado com sucesso! Nome: {nome}, Email: {email}")
    elif request.method == 'GET':
        html = '''
            <html>
                <head>
                    <title>Cadastro de Usuário</title>
                </head>
                <body>
                <h1>Cadastro de Usuário</h1>
                <form action="/usuarios/cadastro/" method="POST">
                    
                    <label for="nome">Nome:</label><br>
                    <input type="text" name="nome"><br><br>
                    <label for="email">Email:</label><br>
                    <input type="email" name="email"><br><br>
                    <button type="submit">Cadastrar</button>
                </form>
                </body>
            </html>
        '''
        
        return HttpResponse(html)

def perfil_usuario(request, usuario):
    dados = {
        "nome": usuario,
        "idade": 30,
        "email": "rossini@example.com",
        "instagram": "@rossini",
    }
    return JsonResponse(dados)

def mostrar_rota(request):
    rota_completa = request.get_full_path()
    return HttpResponse(f"Rota completa acessada: {rota_completa}")
