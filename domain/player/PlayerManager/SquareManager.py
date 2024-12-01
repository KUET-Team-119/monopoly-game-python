from typing import Dict, List
from domain.square.RailRoadSquare import RailRoadSquare
from domain.square.UtilitySquare import UtilitySquare
from domain.square.LotSquare import LotSquare
from domain.square.PropertySquare import PropertySquare

class SquareManager:
    def __init__(self):
        self._property_squares: Dict[int, PropertySquare] = {}

    def add_property_square(self, index: int, square: PropertySquare) -> None:
        self._property_squares[index] = square

    def count_railroad_squares(self) -> int:
        return sum(1 for square in self._property_squares.values() 
                  if isinstance(square, RailRoadSquare))

    def count_utility_squares(self) -> int:
        return sum(1 for square in self._property_squares.values() 
                  if isinstance(square, UtilitySquare))

    def get_property_squares(self) -> Dict[int, PropertySquare]:
        return self._property_squares

    # 특정 부지를 맵에서 제거
    def remove_property_square(self, index: int) -> None:
        property_square = self._property_squares.get(index)
        if property_square:
            # 부지가 LotSquare라면 집이나 호텔을 제거하는 추가 작업 수행
            if isinstance(property_square, LotSquare):
                lot_square = property_square
                # 부지에 집이나 호텔이 있다면 이를 먼저 처리
                lot_square.destroy_building()

            # 부지를 Map에서 제거
            self._property_squares.pop(index)

    # 부지의 가치를 기준으로 property_squares 정렬
    def get_sorted_property_square(self) -> List[PropertySquare]:
        return sorted(
            self._property_squares.values(),
            key=lambda x: x.get_rent(),
            reverse=True
        )
