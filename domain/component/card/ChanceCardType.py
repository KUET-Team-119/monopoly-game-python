from enum import Enum
from domain.component.card.Card import Card

class ChanceCardType(Enum):
    FORWARD_TO_START_SQUARE = (0, '출발점으로 전진', 0)
    FORWARD_TO_FIRST_RAILROAD_SQUARE = (1, '가장 가까운 철도 칸으로 전진', 0)
    FORWARD_TO_NEAREST_RAILROAD_SQUARE = (2, '가장 가까운 철도 칸으로 전진', 0)
    FORWARD_TO_NEAREST_UTILITY_SQUARE = (3, '가장 가까운 수도/전기 칸으로 전진', 0)
    DEPOSIT_150_CASH = (4, '은행에게 150원 받기', 150)
    DEPOSIT_50_CASH = (5, '은행에게 5원 받기', 50)
    WITHDRAW_15_CASH = (6, '은행에 15원 내기', 15)
    PAY_50_CASH_TO_OTHER_PLAYERS = (7, '다른 사람에게 50원씩 내기', 0)
    GO_BACK = (8, '뒤로 3칸 이동', 0)
    GO_TO_JAIL = (9, '감옥으로 가시오', 0)

    def __init__(self, index: int, name: str, amount: int):
        self._index = index
        self._name = name
        self._amount = amount
    
    @property
    def index(self) -> int:
        return self._index
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def amount(self) -> int:
        return self._amount