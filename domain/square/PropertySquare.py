from abc import ABC, abstractmethod
from domain.square.Square import Square
from domain.square.PropertySquare import PropertySquare
from domain.player.Player import Player

class PropertySquare(Square, ABC):
    def __init__(self, index: int, name: str, price: int):
        self._index = index
        self._name = name
        self._price = price
        self._owner = None
        self._sold_out = False

    def landed_on(self, player: Player) -> None:
        if self._owner is None:
            print('주인 없는 땅입니다.')
            if player.cash_manager.has_enough_cash(self._price):
                print('땅을 구매합니다.')
                player.cash_manager.reduce_cash(self._price)
                self._owner = player
                player.square_manager().add_property_square(self._index, self)
            else:
                print('돈이 부족해 땅을 구입할 수 없습니다.')
            return

        if self._owner == player:
            print('본인 소유의 땅입니다.')
            self.manage_square()
            return

        rent = self.rent
        print(f'다른 플레이어 소유의 땅입니다. {rent}원의 임대료를 납부해야 합니다.')
        amount = player.cash_manager().reduce_cash(rent)
        print(f'{amount}원을 플레이어 {self.owner.id}에게 줍니다.')
        self.owner.cash_manager().add_cash(amount)

    @property
    def owner(self) -> Player:
        return self._owner

    @owner.setter
    def owner(self, player: Player) -> None:
        self._sold_out = True
        self._owner = player

    @property
    def price(self) -> int:
        return self.price

    @abstractmethod
    def manage_square(self) -> None:
        pass

    def is_more_expensive(self, square: PropertySquare) -> PropertySquare:
        if self.rent > square.rent:
            return self
        return square

    @abstractmethod
    def rent(self) -> int:
        pass
