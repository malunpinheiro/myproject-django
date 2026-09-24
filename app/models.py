from django.db import models

#tipo string -> CharField()
#tipo inteiro -> IntegerField()
#tipo decimal -> FloatField()
#tipo string -> BooleanField()

# models:

class Produtos(models.Model): #correto -> produto (singular)
    nome = models.CharField(max_length=200)
    preco = models.FloatField() #classe filha (subclasse)
    estoque = models.IntegerField()
    imagem = models.CharField(max_length=500, default= '') #500 representa o tam do link de ref a imagem

    def __str__(self):
        return self.nome #método getter