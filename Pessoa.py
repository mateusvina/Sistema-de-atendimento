
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.prioritario = self.definir_prioridade()

    def definir_prioridade(self):
        return self.idade >= 55 or self.idade <= 2

    def __str__(self):
        tipo = "Prioritário" if self.prioritario else "Regular"
        return f"{self.nome} (Idade: {self.idade}) - {tipo}"