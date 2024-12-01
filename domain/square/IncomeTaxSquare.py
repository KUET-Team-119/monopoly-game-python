from typing import Final
from domain.player.Player import Player
from domain.square.Square import Square

class IncomeTaxSquare(Square):
    TAX: Final = 200

    def __init__(self, index: int, name: str):
        self._index = index
        self._name = name

    def landed_on(self, player: Player) -> None:
        print(f'소득세 {IncomeTaxSquare.TAX}원을 납부하세요.')
        player.cash_manager.reduce_cash(IncomeTaxSquare)