from typing import Final
from domain.square.PropertySquare import PropertySquare

class RailRoadSquare(PropertySquare):

    RAILROAD_RENT = 25

    def __init__(self, index: int, name: str, price:int):
        super().__init__(index, name, price)
    
    def rent(self) -> int:
        return RailRoadSquare.RAILROAD_RENT * self._owner.square_manager.count_rail_road_square()
    
    def manage_square(self) -> None:
        print(f'{self._name}을 둘러봅니다.')