from models.item import Item

class KnapsackDatasets:
    @staticmethod
    def get_predefined_sets() -> dict:
        """Retorna conjuntos de teste pré-definidos"""
        return {
            "Pequeno": {
                "items": [
                    Item(index=0, weight=2, value=3),
                    Item(index=1, weight=3, value=4)
                ],
                "capacity": 5,
                "description": "Conjunto pequeno (2 itens)"
            },
            "Médio": {
                "items": [
                    Item(index=0, weight=10, value=60),
                    Item(index=1, weight=20, value=100),
                    Item(index=2, weight=30, value=120),
                    Item(index=3, weight=15, value=70),
                    Item(index=4, weight=25, value=110),
                    Item(index=5, weight=35, value=150),
                    Item(index=6, weight=5, value=30),
                    Item(index=7, weight=40, value=160),
                    Item(index=8, weight=50, value=200),
                    Item(index=9, weight=12, value=50)
                ],
                "capacity": 100,
                "description": "Conjunto médio (10 itens)"
            }
        }