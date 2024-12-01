from math import round
from domain.component.building.Building import Building

class House(Building):
    MAX_COUNT_OF_HOUSE: int = 4

    def __init__(self, price: int):
        super().__init__(round(price * 0.1))

    def can_build(self) -> bool:
        return self._count < self.MAX_COUNT_OF_HOUSE