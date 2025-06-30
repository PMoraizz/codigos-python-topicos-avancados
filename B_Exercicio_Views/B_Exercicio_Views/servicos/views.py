from django.http import HttpResponse, JsonResponse

def calcular_desconto(request):
    preco = float(request.GET.get('preco'))
    percentual = float(request.GET.get('desconto'))
    preco_com_desconto = preco * (1 - percentual/100)
    return HttpResponse(f"Preço com desconto: R$ {preco_com_desconto:.2f}")


def mensagem_controle(request, usuario):
    if usuario == "Paulo":
        return HttpResponse(f"{usuario}, você precisa realizar a troca da sua senha.")
    elif usuario == "Pedro":
        return HttpResponse(f"{usuario}, você precisa confirmar o seu email.")
    else:
        return HttpResponse("Não há mensagens pendentes.")
    

def maior(request):
    num1 = int(request.GET.get('n1'))
    num2 = int(request.GET.get('n2'))
    num3 = int(request.GET.get('n3'))
    
    maior_numero = max(num1, num2, num3)
    return HttpResponse(f"O maior número é: {maior_numero}")


def api_info(request):
    dados = {
        "desconto": {"serviço": "Preço com Desconto", "link": "/calcular-desconto/?preco=100&desconto=10"},
        "mensagem":{"serviço": "Mensagem Controle", "link": "/mensagem/Usuario/"},
        "maior": {"serviço": "Maior Número", "link": "/maior/?n1=10&n2=20&n3=30"},
        "api": {"serviço": "API Info", "link": "/api-info/"}
    }
    return JsonResponse(dados)
