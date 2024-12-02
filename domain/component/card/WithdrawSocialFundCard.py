from domain.component.card.SocialFundCard import SocialFundCard
from domain.player.Player import Player

class WithdrawSocialFundCard(SocialFundCard):
    def __init__(self, index: int, name: str, amount: int):
        self._index = index
        self._name = name
        self._amount = amount

    def take_effect(self, player: Player) -> None:
        player.cash_manager.reduce_cash(self._amount)