from domain.MonopolyGame import MonopolyGame
from domain.player.Player import Player
from domain.player.PlayerState.BankruptState import BankruptState
from domain.player.PlayerState.NormalState import NormalState
from domain.player.PlayerState.PlayerState import PlayerState
from domain.player.PlayerState.PrisonState import PrisonState

class StateManager:
    def __init__(self, player: Player):
        self._player = player
        self._state: PlayerState = NormalState(player)

    def become_normal_state(self) -> None:
        self._state = NormalState(self._player)

    def become_prison_state(self) -> None:
        self._state = PrisonState(self._player)

    def become_bankrupt_state(self) -> None:
        self._state = BankruptState()
        MonopolyGame.handle_bankrupt_player(self._player)

    def is_normal_state(self) -> bool:
        return isinstance(self._state, NormalState)

    def is_bankrupt_state(self) -> bool:
        return isinstance(self._state, BankruptState)

    @property
    def state(self) -> PlayerState:
        return self._state