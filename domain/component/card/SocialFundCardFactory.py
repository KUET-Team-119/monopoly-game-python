from domain.component.card.Card import Card
from domain.component.card.SocialFundCard import SocialFundCard
from domain.component.card.SocialFundCardType import SocialFundCardType
from domain.component.card.DepositSocialFundCard import DepositSocialFundCard
from domain.component.card.WithdrawSocialFundCard import WithdrawSocialFundCard
from domain.component.card.ForwardToStartSocialFundCard import ForwardToStartSocialFundCard
from domain.component.card.ForwardToFirstRailRoadChanceCard import ForwardToFirstRailRoadChanceCard
from domain.component.card.GoToJailSocialFundCard import GoToJailSocialFundCard

class SocialFundCardFactory:
    index_counter: int = -1
    
    @classmethod
    def create_social_fund_card(cls, social_fund_card_type: SocialFundCardType) -> SocialFundCard:
        cls.index_counter += 1
        index = cls.index_counter

        match social_fund_card_type:
            case SocialFundCardType.DEPOSIT_10_CASH | SocialFundCardType.DEPOSIT_20_CASH | SocialFundCardType.DEPOSIT_25_CASH | \
                 SocialFundCardType.DEPOSIT_50_CASH | SocialFundCardType.DEPOSIT_100_CASH | SocialFundCardType.DEPOSIT_200_CASH:
                return DepositSocialFundCard(index, social_fund_card_type.name, social_fund_card_type.amount)
            
            case SocialFundCardType.WITHDRAW_50_CASH | SocialFundCardType.WITHDRAW_100_CASH | SocialFundCardType.WITHDRAW_150_CASH:
                return WithdrawSocialFundCard(index, social_fund_card_type.name, social_fund_card_type.amount)
            
            case SocialFundCardType.FORWARD_TO_START_SQUARE:
                return ForwardToStartSocialFundCard(index, social_fund_card_type.name)
            
            case SocialFundCardType.RECEIVE_10_CASH_FROM_OTHER_PLAYERS:
                return ForwardToFirstRailRoadChanceCard(index, social_fund_card_type.name, social_fund_card_type.amount)
            
            case SocialFundCardType.GO_TO_JAIL:
                return GoToJailSocialFundCard(index, social_fund_card_type.name)
            
            case _:
                raise ValueError(f'알 수 없는 사회기금 카드 유형: {social_fund_card_type}')