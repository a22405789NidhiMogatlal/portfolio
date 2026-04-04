from django.db import models

# Create your models here.

class Licenciatura(models.Model):
    nome=models.CharField(max_length=255)
    duracao=models.IntegerField()
    urlSite=models.CharField(max_length=255)
    objetivos=models.TextField()
    
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
    ano=models.IntegerField()
    semestre=models.IntegerField()
    ects=models.IntegerField()
    apresentacao=models.TextField()
    programa=models.TextField()
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
    tipo=models.CharField(max_length=50,choices=TIPO_CHOICES)
    logo=models.ImageField(upload_to='tecnologias/',blank=True,null=True)
    urlSite = models.URLField(blank=True)
    nivel=models.IntegerField(choices=NIVEL_CHOICES)
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
    categoria = models.ForeignKey('CategoriaCompetencia', on_delete=models.SET_NULL,null=True,blank=True,related_name='competencias' )

    def __str__(self):
        return self.nome




    



