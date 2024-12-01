from typing import Final
from domain.player.Player import Player
from domain.square.Square import Square

class StartSquare(Square):

    SALARY: Final = 200
    
    def __init__(self, index: int, name: str):
        self._index = index
        self._name = name
    
    def landed_on(self, player: Player) -> None:
        print(f'월급 {StartSquare.SALARY}원을 받아가세요.')
        player.cash_manager.add_cash(StartSquare.SALARY)