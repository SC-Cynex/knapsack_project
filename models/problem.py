from dataclasses import dataclass
from typing import List
from .item import Item

@dataclass
class KnapsackProblem:
    """Modelo contendo a definição completa do problema"""
    items: List[Item]
    capacity: int
    description: str = "Problema da Mochila Padrão"

    @property
    def total_items(self) -> int:
        return len(self.items)

    def validate(self) -> bool:
        return all(item.weight > 0 for item in self.items) and self.capacity > 0