from domain.component.Board import Board
from domain.component.building.Hotel import Hotel
from domain.component.building.House import House
from domain.square.PropertySquare import PropertySquare

class LotSquare(PropertySquare):
    def __init__(self, index: int, name: str, price: int):
        super().__init__(index, name, price)
        self._house = House(price)
        self._hotel = Hotel(price)

    def manage_square(self) -> None:
        if self._can_build_house():
            print('주택을 짓습니다.')
            self._house.build()
            Board.add_count_of_house()
            self.owner.cash_manager.reduce_cash(self.house.price)
        elif self._can_build_hotel():
            print('호텔을 짓습니다.')
            self._hotel.build()
            Board.add_count_of_hotel()
            self.owner.cash_manager.reduce_cash(self.hotel.price)
        else:
            print('건물을 지을 수 없습니다.')

    def _can_build_house(self) -> bool:
        return (Board.can_build_house() and 
                self._house.can_build() and 
                self.owner.cash_manager.has_enough_cash(self._house.price))

    def _can_build_hotel(self) -> bool:
        return (Board.can_build_hotel() and 
                not self._house.can_build() and 
                self._hotel.can_build() and 
                self.owner.cash_manager().has_enough_cash(self._hotel.price))

    def destroy_building(self) -> None:
        self._house.destroy()
        self._hotel.destroy()

    @property
    def rent(self) -> int:
        return self.price + self._house.rent + self._hotel.rent

    def sell_to_bank(self) -> int:
        return self._house.sold() + self._hotel.sold() 