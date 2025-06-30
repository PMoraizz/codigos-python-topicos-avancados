from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

def home(request):
    return HttpResponse("Bem-vindo ao Turismo!")

def ponto(request, nome):
    return HttpResponse(f"Você está visitando o ponto turístico: {nome}")

def redirecionar_prefeitura(request):

    return redirect('cidade:prefeitura_padrao')


def pesquisa(request):

    setor = request.GET.get('setor')
    guia = request.GET.get('guia')
    if guia == 'sim':
        return HttpResponse(f"Seguem os resultados para possibilidade de turismo no setor '{setor}' com guia.")
    else:
        return HttpResponse(f"Seguem os resultados para possibilidade de turismo no setor '{setor}' sem guia.")
    