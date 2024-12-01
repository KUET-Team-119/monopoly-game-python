from abc import ABC, abstractmethod

class Building(ABC):
    def __init__(self, price: int):
        self._count: int = 0
        self._price: int = price

    @abstractmethod
    def can_build(self) -> bool:
        pass

    def build(self) -> None:
        self._count += 1

    def destroy(self) -> None:
        self._count = 0

    @property
    def rent(self) -> int:
        return self._count * self._price

    @property
    def price(self) -> int:
        return self._price

    def sold(self) -> int:
        current_count = self._count
        self._count = 0
        return current_count * self._price
