from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à Cidade!")

def bairro(request, nome):
    return HttpResponse(f"Você está no bairro: {nome}")

def prefeitura(request, prefeito='Maria Silva'):
    return HttpResponse(f"O prefeito é: {prefeito}")
