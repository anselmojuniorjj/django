from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=70)
    sobrenome = models.CharField(max_length=70)
    idade = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    foto = models.ImageField(null=True, blank=True, upload_to='clientes')
    dat_nasc = models.DateField(null=True, blank=True)

    def get_nomeCompleto(self):
        return self.nome + ' ' + self.sobrenome

    def __str__(self):
        return self.get_nomeCompleto()