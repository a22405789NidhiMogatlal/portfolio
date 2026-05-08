from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artigos_view, name='lista_artigos'),

    path('registo/', views.registo_view, name='registo'),

    path('novo/', views.criar_artigo_view, name='criar_artigo'),

    path('<int:id>/', views.detalhe_artigo_view, name='detalhe_artigo'),

    path('<int:id>/editar/', views.editar_artigo_view, name='editar_artigo'),

    path('<int:id>/like/', views.like_artigo, name='like_artigo'),
]