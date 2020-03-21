from django.contrib import messages
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


from .forms import ContatoForm, ProdutoModelForm, EscreverForm
from .models import Produto

# Create your views here.


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def indexcrispy(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'indexcrispy.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            # Para TESTAR
            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # assunto = form.cleaned_data['assunto']
            # mensagem = form.cleaned_data['mensagem']
            #
            # print('Mensagem enviada')
            # print('Nome: {}'.format(nome))
            # print(f'E-mail: {email}')
            # print(f'Assunto: {assunto}')
            # print(f'Mensagem: {mensagem}')

            # Para Enviar
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    # else:
    #     messages.error(request, 'Method GET foi chamado')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def escrever(request):
    form = EscreverForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            # Para TESTAR
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print('Nome: {}'.format(nome))
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            # Para Enviar
            # form.send_mail()

            messages.success(request, 'A1 - E-mail escrever com sucesso!')
            form = EscreverForm(None)
            return HttpResponseRedirect("/escrever/")
        else:
            messages.error(request, 'Erro contato1 enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'escrever.html', context)


def produto(request):
    print(request.user)
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                # Para testar e imprimir no console
                # prod = form.save(commit=False)

                # print(f'Nome: {prod.nome}')
                # print(f'Preço: {prod.preco}')
                # print(f'Estoque: {prod.estoque}')

                # print(f'Imagem: {prod.image}')

                form.save()

                messages.success(request, 'Produto salvo com sucesso!')
                form = ProdutoModelForm()
                return HttpResponseRedirect('/produto/')
            else:
                messages.error(request, 'Erro ao salvar o produto.')
        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('indexcrispy')


def error404(request, ex):
    print(ex)
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
