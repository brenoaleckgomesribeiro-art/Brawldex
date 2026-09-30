from django.db import models


class Brawler(models.Model):
    nome = models.CharField(max_length=100)
    raridade = models.CharField(max_length=50)
    classe = models.CharField(max_length=50)
    vida = models.IntegerField()
    dano = models.IntegerField()
    descricao = models.TextField()

    # Arquivo local (upload manual)
    imagem = models.ImageField(
        upload_to='brawlers/',
        blank=True,
        null=True
    )

    # URL externa (preenchida pelo admin quando quiser)
    # Se existir imagem local, ela tem prioridade.
    imagem_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='URL da imagem'
    )

    def __str__(self):
        return self.nome