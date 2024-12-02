from domain.component.card.ChanceCard import ChanceCard
from domain.player.Player import Player
from domain.MonopolyGame import MonopolyGame

class PayToOtherPlayersChanceCard(ChanceCard):
    def __init__(self, index: int, name: str, payment: int):
        self._index = index
        self._name = name
        self._payment = payment

    def take_effect(self, player: Player) -> None:
        for other_player in MonopolyGame.players.values():
            if player == other_player or other_player.state_manager.is_bankrupt_state():
                continue
            
            amount = player.cash_manager.reduce_cash(self._payment)
            print(f'{other_player.id}에게 돈을 {amount}만큼 줍니다.')
            other_player.cash_manager.add_cash(amount)