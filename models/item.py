from dataclasses import dataclass

@dataclass
class Item:
    """Modelo que representa um item da mochila"""
    index: int
    weight: int
    value: int

    def value_density(self) -> float:
        """Calcula a razão valor/peso"""
        return self.value / max(self.weight, 0.001)

    def __str__(self):
        return f"Item {self.index} (Peso: {self.weight}, Valor: {self.value})"