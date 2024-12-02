from domain.square.Square import Square
from domain.square.UtilitySquare import UtilitySquare
from domain.component.card.ForwardToNearestChanceCard import ForwardToNearestChanceCard

class ForwardToNearestUtilityChanceCard(ForwardToNearestChanceCard):
    def __init__(self, index: int, name: str):
        super().__init__(index, name)
    
    def get_target_square_class(self) -> type[Square]:
        return UtilitySquare