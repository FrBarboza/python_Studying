from django.urls import path
# from .views import index, contact
from django.conf.urls import handler400, handler500
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('produto/<int:pk>', views.produto, name='produto')
]

handler404 = views.error404
handler500 = views.error500
