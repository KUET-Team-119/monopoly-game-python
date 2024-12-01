from math import round
from domain.component.building.Building import Building

class Hotel(Building):
    MAX_COUNT_OF_HOTEL: int = 1

    def __init__(self, price: int):
        super().__init__(round(price * 0.4))

    def can_build(self) -> bool:
        return self._count < self.MAX_COUNT_OF_HOTEL