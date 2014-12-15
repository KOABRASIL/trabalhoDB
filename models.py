from django.db import models

class ZonaEleitoral(models.Model)
	sigla = models.Chars.Field(max_length=2)
	nome = models.Chars.Field(max_length=30)

class Candidato(models.Model):
    NOME = models.CharField(max_length=200)
    NOME_URNA = models.CharField(max_length=30)
    ID_NUMERO = models.IntegerField()
    ID_CARGO = models.CharField(max_length=30)
    ID = ID_NUMERO
