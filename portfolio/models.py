from django.db import models

# Create your models here.

class Licenciatura(models.Model):
    nome=models.CharField(max_length=255,)
    duracao=models.IntegerField(blank=True, null=True)
    urlSite=models.CharField(max_length=255, blank=True)
    objetivos=models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    imagem = models.ImageField(upload_to='docentes/', blank=True, null=True)
    
    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    nome=models.CharField(max_length=255)
    ano=models.IntegerField(blank=True)
    semestre=models.IntegerField(blank=True)
    ects=models.IntegerField(blank=True)
    apresentacao=models.TextField(blank=True)
    programa=models.TextField(blank=True)
    licenciaturas=models.ManyToManyField(Licenciatura,blank=True,related_name="unidadesCurriculares")
    docentes=models.ManyToManyField(Docente,blank=True,related_name="unidadesCurriculares")
    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    TIPO_CHOICES=[
        ('linguagem','Linguagem de Programação'),
        ('framework', 'Framework'),
        ('base_dados', 'Base de Dados'),
        ('ferramenta', 'Ferramenta'),
        ('devops', 'DevOps'),
        ('outro', 'Outro'),
    ]

    NIVEL_CHOICES=[
        (1, '1 - Básico'),
        (2, '2 - Elementar'),
        (3, '3 - Intermédio'),
        (4, '4 - Avançado'),
        (5, '5 - Especialista'), 

    ]

    nome=models.CharField(max_length=255)
    tipo=models.CharField(max_length=50,choices=TIPO_CHOICES,blank=True)
    logo=models.ImageField(upload_to='tecnologias/',blank=True,null=True)
    urlSite = models.URLField(blank=True)
    nivel=models.IntegerField(choices=NIVEL_CHOICES,blank=True,default=3)
    aspetosRelavantes=models.TextField(blank=True)

    def __str__(self):
        return self.nome

class CategoriaCompetencia(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey('CategoriaCompetencia', on_delete=models.SET_NULL,  null=True,blank=True,related_name='competencias' )

    def __str__(self):
        return self.nome

class Tfc(models.Model): 
    
    CLASSIFICACAO_CHOICES = [
        (1, '1 - Pouco interessante'),
        (2, '2 - Interessante'),
        (3, '3 - Moderadamente interessante'),
        (4, '4 - Muito interessante'),
        (5, '5 - Extremamente interessante'),
    ]
    titulo = models.CharField(max_length=255)
    alunos = models.TextField(max_length=255, blank=True)
    orientadores= models.ManyToManyField(Docente, blank=True, related_name='tfcs')
    ano = models.IntegerField()
    url_relatorio = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    areas=models.TextField(blank=True)
    imagem = models.ImageField(upload_to='tfcs/', blank=True, null=True)
    classificacao = models.IntegerField(choices=CLASSIFICACAO_CHOICES, default=3)
    licenciatura=models.ManyToManyField(Licenciatura,related_name='tfcs')
    tecnologia=models.ManyToManyField(Tecnologia,related_name='tfcs')


class Projeto(models.Model):
    TIPO_CHOICES = [
        ('UC', 'Unidade Curricular'),
        ('PESSOAL', 'Pessoal'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    urlVideo = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True)
    conceitos = models.TextField(blank=True)
    urlGithub = models.URLField(blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='projetos')
    uc = models.ForeignKey('UnidadeCurricular', on_delete=models.SET_NULL, null=True,blank=True,related_name='projetos')

    def __str__(self):
        return self.titulo


class Formacao(models.Model):
    titulo = models.CharField(max_length=255)
    instituicao = models.CharField(max_length=255, blank=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_conclusao = models.DateField(blank=True, null=True)
    certificado = models.ImageField(upload_to='certificados/', blank=True)


    def __str__(self):
        return self.titulo
    
class MakingOf(models.Model):
    ENTIDADE_CHOICES = [
        ('licenciatura', 'Licenciatura'),
        ('uc', 'Unidade Curricular'),
        ('docente', 'Docente'),
        ('projeto', 'Projeto'),
        ('tecnologia', 'Tecnologia'),
        ('tfc', 'TFC'),
        ('competencia', 'Competência'),
        ('categoria_competencia', 'Categoria Competência'),
        ('formacao', 'Formação'),
        ('makingof', 'MakingOf'),
        ('geral', 'Geral'),
    ]

    titulo = models.CharField(max_length=255)
    entidade = models.CharField(max_length=50, choices=ENTIDADE_CHOICES, default='geral')
    descricao = models.TextField(blank=True)
    justificacao = models.TextField(blank=True)
    erros = models.TextField(blank=True)
    correcoes = models.TextField(blank=True)
    usoIa = models.TextField(blank=True)
    foto = models.ImageField(upload_to='makingof/', blank=True, null=True)
    dataRegisto = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
