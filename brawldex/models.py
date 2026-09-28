from django.db import models


class Brawler(models.Model):
    nome = models.CharField(max_length=100)
    raridade = models.CharField(max_length=50)
    classe = models.CharField(max_length=50)
    vida = models.IntegerField()
    dano = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='brawlers/', blank=True, null=True)

    def __str__(self):
        return self.nome