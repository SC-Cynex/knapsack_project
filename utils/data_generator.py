import random
from models.item import Item

class DataGenerator:
    @staticmethod
    def generate_random_items(num_items: int, max_weight=100, max_value=100) -> list[Item]:
        """Gera itens aleatórios para testes"""
        return [
            Item(index=i, weight=random.randint(1, max_weight), 
                   value=random.randint(1, max_value))
            for i in range(num_items)
        ]

    @staticmethod
    def calculate_capacity(items: list[Item], ratio=0.4) -> int:
        """Calcula capacidade baseada no peso total"""
        return int(sum(item.weight for item in items) * ratio)