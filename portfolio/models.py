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



