from domain.player.Player import Player
from domain.square.Square import Square

class FreeParkingSquare(Square):

    def __init__(self, index: int, name: str):
        self._index = index
        self._name = name

    def landed_on(self, player: Player) -> None:
        print('무료 주차장입니다.')