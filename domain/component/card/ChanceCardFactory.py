from domain.component.card.Card import Card
from domain.component.card.ChanceCard import ChanceCard
from domain.component.card.ChanceCardType import ChanceCardType

class ChanceCardFactory:
    index_counter: int = -1
    
    @classmethod
    def create_chance_card(cls, chance_card_type: ChanceCardType) -> ChanceCard:
        cls.index_counter += 1
        index = cls.index_counter

        match chance_card_type:
            case ChanceCardType.DEPOSIT_50_CASH | ChanceCardType.DEPOSIT_150_CASH:
                return DepositChanceCard(index, chance_card_type.name, chance_card_type.amount)
            
            case ChanceCardType.WITHDRAW_15_CASH:
                return WithdrawChanceCard(index, chance_card_type.name, chance_card_type.amount)
            
            case ChanceCardType.FORWARD_TO_START_SQUARE:
                return ForwardToStartChanceCard(index, chance_card_type.name)
            
            case ChanceCardType.FORWARD_TO_FIRST_RAILROAD_SQUARE:
                return ForwardToFirstRailRoadChanceCard(index, chance_card_type.name)
            
            case ChanceCardType.FORWARD_TO_NEAREST_RAILROAD_SQUARE:
                return ForwardToNearestRailRoadChanceCard(index, chance_card_type.name)
            
            case ChanceCardType.FORWARD_TO_NEAREST_UTILITY_SQUARE:
                return ForwardToNearestUtilityChanceCard(index, chance_card_type.name)
            
            case ChanceCardType.PAY_50_CASH_TO_OTHER_PLAYERS:
                return PayToOtherPlayersChanceCard(index, chance_card_type.name, chance_card_type.amount)
            
            case ChanceCardType.GO_BACK:
                return GoBackChanceCard(index, chance_card_type.name)
            
            case ChanceCardType.GO_TO_JAIL:
                return GoToJailChanceCard(index, chance_card_type.name)
            
            case _:
                raise ValueError(f'알 수 없는 찬스 카드 유형: {chance_card_type}')