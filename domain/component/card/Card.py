from abc import ABC, abstractmethod
from domain.player.Player import Player

class Card(ABC):

    def __init__(self):
        self._index: int
        self._name: str
    
    @abstractmethod
    def take_effect(self, player: Player) -> None:
        pass