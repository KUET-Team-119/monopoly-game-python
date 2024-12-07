from typing import Final
from domain.square.LotSquare import LotSquare
from player.Player import Player

class CashManager:
    
    INITIAL_CASH: Final = 1_500

    def __init__(self, player: Player):
        self._player = player
        self._cash = CashManager.INITIAL_CASH

    def add_cash(self, amount: int) -> None:
        print(f'{amount}원을 받습니다.')
        self._cash += amount

    def reduce_cash(self, amount: int) -> int:
        print(f'가진 돈은 {self._cash}원입니다.')
        if self.has_enough_cash(amount):
            return self.reduce_available_cash(amount)
        return self.handle_insufficient_cash(amount)

    def reduce_available_cash(self, amount: int) -> int:
        self._cash -= amount
        return amount

    def handle_insufficient_cash(self, amount: int) -> int:
        self.cover_cash(amount)

        if self.has_enough_cash(amount):
            return self.reduce_available_cash(amount)
        return self.handle_bankruptcy()

    def handle_bankruptcy(self) -> int:
        print(f'플레이어 {self._player.id}이/가 파산했습니다.')
        self._player.state_manager.become_bankrupt_state()
        payable_amount = self._cash
        self._cash = 0
        return payable_amount
    
    def cover_cash(self, amount: int) -> None:
        sorted_property_squares = self._player.square_manager.get_sorted_property_square()
        total_cash = self._cash
    
        # 정렬된 부지들을 순차적으로 처리
        for property_square in sorted_property_squares:
            value = property_square.rent if isinstance(property_square, LotSquare) else property_square.price
            total_cash += value
            self._player.square_manager.remove_property_square(property_square.index)
    
            # 현금이 목표 금액 이상이 되면 판매 중지
            if total_cash >= amount:
                self._cash = total_cash - amount  # 초과한 금액은 플레이어의 현금으로 남김
                return
    
        # 모든 부지를 팔고도 부족하다면, 남은 현금 설정
        self._cash = total_cash

    def has_enough_cash(self, amount: int) -> bool:
        return self._cash >= amount

    def calculate_total_assets(self) -> int:
        self.cover_cash(int(1e9))
        return self._cash
    
    @property
    def cash(self) -> int:
        return self._cash