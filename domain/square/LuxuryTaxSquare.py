from typing import Final
from domain.player.Player import Player
from domain.square.Square import Square

class LuxuryTaxSquare(Square):
    TAX: Final = int(1e9)

    def __init__(self, index: int, name: str):
        self._index = index
        self._name = name

    def landed_on(self, player: Player) -> None:
        print(f'사치세 {LuxuryTaxSquare.TAX}원을 납부하세요.')
        player.cash_manager.reduce_cash(LuxuryTaxSquare.TAX)