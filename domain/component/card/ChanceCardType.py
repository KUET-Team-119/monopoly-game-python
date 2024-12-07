from domain.component.card.CardType import CardType

class ChanceCardType(CardType):
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
        super().__init__(index, name, amount)