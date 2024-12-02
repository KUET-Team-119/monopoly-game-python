from typing import Final
from domain.component.card.ChanceCard import ChanceCard
from domain.player.Player import Player
from domain.square.SquareType import SquareType

class GoBackChanceCard(ChanceCard):

    steps: Final = 3

    def __init__(self, index: int, name: str):
        self._index = index
        self._name = name
    
    def take_effect(self, player: Player) -> None:
        player.piece_moving_manager.move_backward_by_steps(GoBackChanceCard.steps)