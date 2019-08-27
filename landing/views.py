from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.

def retornar_index(request):
    primeiro_nome = 'GROGERIN'
    sobrenome = 'Joano'

    contexto = {
        'nome': primeiro_nome,
        'sobrenome': sobrenome
    }
    return render(request, 'index.html', contexto)

def sobre(request):
    salada_de_frutas = ['Atemoia', 'Kiwi', 'Mamão', 'Abacate']
    nome = 'groger'
    if nome == 'groger':
        status = 'iai groger'
    elif nome:
        status = 'preenchido'
    else:
        status = 'não sei seu nome'

    contexto = {
        'salada_de_frutas': salada_de_frutas,
        'batatinha': nome.lower(),
        'status': status
    }
    return render(request, 'sobre.html', contexto)
