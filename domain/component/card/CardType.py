from enum import Enum

class CardType(Enum):
    
    def __init__(self, index: int, name: str, amount: int):
        self._index = index
        self._name = name
        self._amount = amount
    
    @property
    def index(self) -> int:
        return self._index
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def amount(self) -> int:
        return self._amount