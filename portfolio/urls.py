from django.urls import path

from . import views

urlpatterns = [
    path('', views.licenciaturas_view),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('licenciatura/<int:id>/', views.licenciatura_view, name='licenciatura'),

    path('docentes/', views.docentes_view, name='docentes'),
    path('docente/<int:id>/', views.docente_view, name='docente'),

    path('ucs/', views.ucs_view, name='ucs'),
    path('uc/<int:id>/', views.uc_view, name='uc'),

    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologia/<int:id>/', views.tecnologia_view, name='tecnologia'),
    path('tecnologias/novo/', views.tecnologia_novo_view, name='tecnologia_novos'),

    path('competencias/', views.competencias_view, name='competencias'),
    path('competencia/<int:id>/', views.competencia_view, name='competencia'),
    
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('tfc/<int:id>/', views.tfc_view, name='tfc'),

    path('projetos/', views.projetos_view, name='projetos'),
    path('projeto/<int:id>/', views.projeto_view, name='projeto'),
    path('projetos/novo', views.projeto_novo, name='projeto_novos'),

    path('formacoes/', views.formacoes_view, name='formacoes'),

    path('makingofs/', views.makingofs_view, name='makingofs'),

    path('eventos/', views.eventos_view, name='eventos'),
    path('evento/<int:id>/', views.evento_view, name='evento'),
]