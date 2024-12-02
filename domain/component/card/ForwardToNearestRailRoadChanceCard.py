from domain.component.card.ForwardToNearestChanceCard import ForwardToNearestChanceCard
from domain.square.RailRoadSquare import RailRoadSquare

class ForwardToNearestRailRoadChanceCard(ForwardToNearestChanceCard):
    def __init__(self, index: int, name: str):
        super().__init__(index, name)

    def get_target_square_class(self):
        return RailRoadSquare