from django.urls import path
from django.views.generic import RedirectView
from produto import views


urlpatterns = [
    path('produto/', views.lista_produto),
    path('produto/lista/', views.json_lista_produto),
    path('produto/lista_externa/<int:id_usuario>/', views.json_lista_por_url),
    path('produto/cadastro/', views.cadastro),
    path('produto/cadastro/submit', views.submit_cadastro),
    path('produto/cadastro/delete/<int:id_produto>/', views.delete_cadastro),
    path('', RedirectView.as_view(url='/produto/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user)
]
