from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=[('F', 'Feminino'), ('M', 'Masculino')])
    servicos = models.ManyToManyField(Servico)
    preco = models.DecimalField(max_digits=8, decimal_places=2, editable=False)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    horario = models.DateTimeField()

    def save(self, *args, **kwargs):
        # A lógica do preço deve ser calculada **após o salvamento inicial do cliente**
        # Isso impede chamadas recursivas
        is_new = self.pk is None  # Verifica se é uma instância nova (não salva ainda)
        super().save(*args, **kwargs)  # Primeiro salva o cliente

        if is_new:
            # Só calcula o preço e salva novamente se o cliente for novo
            self.preco = sum([servico.preco for servico in self.servicos.all()])
            super().save(*args, **kwargs)  # Salva novamente após o cálculo do preço

    def __str__(self):
        return f"{self.nome} ({self.pk})"
