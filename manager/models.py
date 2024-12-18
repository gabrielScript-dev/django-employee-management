from django.db import models

class Funcionario(models.Model):
    
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    remuneracao = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        null=False,
        blank=False
    )

    objetos = models.Manager()