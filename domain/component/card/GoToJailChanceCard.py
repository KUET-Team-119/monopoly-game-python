from domain.component.card.ChanceCard import ChanceCard
from domain.player.Player import Player
from domain.square.SquareType import SquareType

class GoToJailChanceCard(ChanceCard):

    def __init__(self, index: int, name: str):
        self._index = index
        self._name = name
    
    def take_effect(self, player: Player) -> None:
        player.piece_moving_manager.warp_to_square_type(SquareType.JAIL)