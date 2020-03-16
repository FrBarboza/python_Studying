from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto


# Create your views here.


def index(request):
    # print(dir(request.user))
    # print(f'InfoUSER: {request.user}')
    # print(f"User: {request.user} Password: {request.user.password}\nUltimo Login: {request.user.last_login} ")
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação Python - templates',
        'outro': 'Outro texto inserido atraves de dicionário',
        'produtos': produtos
    }
    # print(f'Request: {request.POST} Contexto: {context}')
    return render(request, 'index.html', context)


def contato(request):
    print(request)
    print(request.POST)
    return render(request, 'contato.html')


def produto(request, pk):
    # context = {}
    # try:
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    # except Exception as ex:
    #     print(ex)
    #     template = loader.get_template('404.html')
    #     return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)
    return render(request, 'produto.html', context)


# def error404(request, ex):
#    return render(request, '404.html')


def error404(request, ex):
    print(ex)
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
