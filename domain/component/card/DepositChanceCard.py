from domain.component.card.ChanceCard import ChanceCard
from domain.player.Player import Player

class DepositChanceCard(ChanceCard):

    def __init__(self, index: int, name: str, amount: int):
        self._index = index
        self._name = name
        self._amount = amount

    def take_effect(self, player: Player) -> None:
        player.cash_manager.add_cash(self._amount)