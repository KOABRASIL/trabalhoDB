from django.db import models

class ZonaEleitoral(models.Model)
	sigla = models.Chars.Field(max_length=2)
	nome = models.Chars.Field(max_length=30)

