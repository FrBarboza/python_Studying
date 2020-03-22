# Python Studying

#### Criando um Virtual Python Environment
 
> Criar diretório ou pasta
>
```bash
python -m venv <nome da virtual env>
```
#### **Usando Virtual Env (venv)**
>Ativando o VirtualEnv
>
```git
"nome da pasta"/Scripts/activate
```
>Desativando o VirtualEnv
>
```   
"nome da pasta"/Scripts/deactivate
```
#### Instalar django com bootstrap e outros
```bash
    pip install django whitenoise gunicorn django-bootstrpa4 PyMySQL django-stdimage
```
#### Upgrade Pip (Python)
```bash
python -m pip install --upgrade pip
```
#### Instalar MySQL
> Ubuntu
```bash
sudo apt-get install libmysqlclient-dev python3-dev
```
> Mac
```
brew install mysql-connector-c
```
> Windows
> >Instalando o servidor MySQL no Windows, as bibliotecas
    já estarão instaladas.
>
[Download MySQL Install](https://dev.mysql.com/downloads/mysql/)
  
####Usando o GIT
> Na pasta do projeto criar o controle Git
>
```git
git init
```
> A cada mudança deve adicionar as alterações
>
> ponto (.) é para todos os arquivo ou nome do arquivo 
    (no lugar do ponto) que deseja adicionar.
```git
git add .
``` 
> O mais preciso e real das mudanças que estão sendo comitadas.
```
git commit - m "Descrição do commit"
```
> Atualizar o remote (repositório Git no GitHub)
```
git push -u origin master
```        
> Adicionar repositorio Origin ao repositorio GitHub
> pegar o ssh ou https no repositório.
```
git remote add origin git@github.com:xxxxxxxxx/yyyyyyyyyy.git
```
> Para verificar o repositorio remoto ativo
```
git remote -v
```

#### Configurar o DJANGO

> ##### Criar projeto (para não criar estrutura use o . (ponto) 
> ##### após o nome do projeto ( raiz do projeto ))
```
django-admin startproject <nome do project> .
```    
> ##### Criar app (deve-se estar dentro da pasta do projeto)
```
django-admin startapp <nome do app>
```
> ##### Install local (MySql) para usar configuração no Heroku
```
pip install dj_database_url psycopg2-binary
```
> #### **Bootstrap4 Django**
>> Instalar 
```bash
pip install django-bootstrap4
```
>> Importar no template
```html
{% load bootstrap4 %}
```
> ##### **Gerar requirements**
```bash
pip freeze > requirements.txt
```
> ##### **Configurar Settings**
```django
INSTALLED_APPS = [
# Deve ter todas as aplicacoes
# no caso de bootstrap colocar <sua(s) aplicacao(oes)>
...
'bootstrap4',
'stdimage',
]
```
```django
MIDDLEWARE = [
    #Para trabalhar com WhiteNoise, na segunda linha coloque
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
```
```django
TEMPLATES = [
    'DIRS': ['templates']
]
```
#### **Database**
##### https://docs.djangoproject.com/en/3.0/ref/settings/#databases
> SqlLite
```django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
> MySQL
```django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
> PostgreSQL
```django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fusion',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
> PostgreSQL com Heroku
```django
DATABASES = {
    'default': dj_database_url.config()
}
```
> Install local (MySql) para usar configuração no Heroku
```bash
pip install dj_database_url psycopg2-binary
```
