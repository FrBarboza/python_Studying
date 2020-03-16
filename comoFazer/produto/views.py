from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from produto.models import Produto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404, JsonResponse


# Create your views here.

# Format 1
# from django.shortcuts import render, redirect
# outra forma
# def index(request):
#    return redirect('produto/')


def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    # else:
    return redirect('/')


@login_required(login_url='/login/')
def submit_cadastro(request):
    if request.POST:
        nome = request.POST.get('nome')
        nota = request.POST.get('nota')
        tempo_validade = request.POST.get('tempo_validade')
        usuario = request.user
        id_produto = request.POST.get('id_produto')
        if id_produto:
            # Validar com mais seguranca
            produto = Produto.objects.get(id=id_produto)
            if produto.usuario == usuario:
                produto.nome = nome
                produto.nota = nota
                produto.tempo_validade = tempo_validade
                produto.save()

        # Essa validação corre o risco de fazer alteração pela URL de outro usuário
        #    Produto.objects.filter(id=id_produto).update(nome=nome,
        #                                                 nota=nota,
        #                                                 tempo_validade=tempo_validade)
        else:
            Produto.objects.create(nome=nome,
                                   nota=nota,
                                   tempo_validade=tempo_validade,
                                   usuario=usuario)

    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def lista_produto(request):
    usuario = request.user
    produto = Produto.objects.filter(usuario=usuario)
    # print(type(produto))
    dados = {'produtos': produto}
    return render(request, 'cadastro_produtos.html', dados)


@login_required(login_url='/login/')
def cadastro(request):
    id_produto = request.GET.get('id')
    # print(id_produto)
    dados = {}
    try:
        if id_produto:
            dados['produto'] = Produto.objects.get(id=id_produto)
            # if request.user != dados['produto'].usuario:
            #     #dados = {}
            #     raise Http404()

    except Exception:
        raise Http404()
    return render(request, 'cadastro.html', dados)


@login_required(login_url='/login/')
def delete_cadastro(request, id_produto):
    usuario = request.user
    try:
        produto = Produto.objects.get(id=id_produto)
    except Exception:
        raise Http404()
    if usuario == produto.usuario:
        produto.delete()
    else:
        raise Http404()

    return redirect('/')


@login_required(login_url='/login/')
def json_lista_produto(request):
    usuario = request.user
    produto = Produto.objects.filter(usuario=usuario).values('id', 'nome')
    # Por estar passando lista, se fosse dicionário não seria necessário o safe
    # return JsonResponse({'Produto':'Teste'}) #Roda sem problemas
    return JsonResponse(list(produto), safe=False)


def json_lista_por_url(request, id_usuario):
    try:
        usuario = User.objects.get(id=id_usuario)
        produto = Produto.objects.filter(usuario=usuario).values('id', 'nome', 'tempo_validade')
    except Exception:
        raise Http404()
    return JsonResponse(list(produto), safe=False)
