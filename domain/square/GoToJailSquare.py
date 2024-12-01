from domain.player.Player import Player
from domain.square.Square import Square
from domain.square.SquareType import SquareType

class GoToJailSquare(Square):
    
    def __init__(self, index: int, name: str):
        self._index = index
        self._name = name

    def landed_on(self, player: Player) -> None:
        print('감옥으로 가세요.')
        player.piece_moving_manager.warp_to_square_type(SquareType.JAIL)
        player.state_manager.become_prison_state()