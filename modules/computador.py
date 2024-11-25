import random


class Computador:
    COMPONENTES_CONFIG = {
        "cpu": {"preco": 500, "reducao_vida": 0.2},
        "memoria": {"preco": 400, "reducao_vida": 0.3},
        "placa_mae": {"preco": 400, "reducao_vida": 0.5},
        "memoria_ram": {"preco": 200, "reducao_vida": 0.4},
        "fonte": {"preco": 150, "reducao_vida": 0.8}
    }

    def __init__(self, id):
        if id not in Computador.COMPONENTES_CONFIG:
            raise ValueError(f"Componente '{id}' não reconhecido.")
        self.id = id
        self.tempo_de_vida = 100
        self.quebrado = False
        self.preco = Computador.COMPONENTES_CONFIG[id]["preco"]
        self.reducao_vida = Computador.COMPONENTES_CONFIG[id]["reducao_vida"]

    def vidautil(self):
        self.tempo_de_vida -= self.reducao_vida
        if self.tempo_de_vida <= 0:
            self.quebrado = True

    def quebrar_aleatorio(self):
        if random.randint(0, 9) == 9:
            self.quebrado = True

    def __str__(self):
        return (f"{self.id}: Durabilidade {self.tempo_de_vida:.1f}% - "
                f"Quebrado: {self.quebrado}")
