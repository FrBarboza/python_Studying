from django.urls import path
from django.conf.urls import handler404, handler500

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('produto/', views.produto, name='produto'),
]


handler404 = views.error404
handler500 = views.error500
