from django.urls import path
from produto import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.lista_produto),
    path('lista/', views.json_lista_produto),
    path('lista_externa/<int:id_usuario>/', views.json_lista_por_url),
    path('cadastro/', views.cadastro),
    path('cadastro/submit', views.submit_cadastro),
    path('cadastro/delete/<int:id_produto>/', views.delete_cadastro),
    path('', RedirectView.as_view(url='/produto/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user)
]
