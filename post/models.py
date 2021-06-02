from django.db import models

# posts
class Materia(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    data_publicacao = models.DateField('data publicacao')
    img_post = models.ImageField(upload_to='img/', blank=True)
    texto_post = models.TextField()
    

class Relacionada(models.Model):
    materia_relacionada = models.ForeignKey(Materia, on_delete=models.CASCADE)
    observacao = models.CharField(max_length=200)


