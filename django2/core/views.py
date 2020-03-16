from django.contrib import messages
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from . import forms
# Create your views here.


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = forms.ContatoForm(request.POST or None)

    if str(request.method == 'POST'):
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
            form = forms.ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')


def error404(request, ex):
    print(ex)
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
