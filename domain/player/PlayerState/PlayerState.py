from abc import ABC, abstractmethod

class PlayerState(ABC):

    @abstractmethod
    def take_turn(self) -> None:
        pass