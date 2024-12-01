from abc import ABC, abstractmethod
from domain.player.Player import Player

class Square(ABC):
    def __init__(self):
        self._index: int
        self._name: str
    
    @property
    def index(self) -> int:
        return self._index
    
    @property
    def name(self) -> str:
        return self._name
    
    @abstractmethod
    def landed_on(self, player: Player) -> None:
        pass