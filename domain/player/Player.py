from typing import Deque
from domain.component.card.Card import Card
from domain.player.PlayerManager.StateManager import StateManager
from domain.player.PlayerManager.CashManager import CashManager
from domain.player.PlayerManager.SquareManager import SquareManager
from domain.player.PlayerManager.DiceRollingManager import DiceRollingManager
from domain.player.PlayerManager.PieceMovingManager import PieceMovingManager

class Player:
    def __init__(self, id: str):
        self._id = id
        self._state_manager = StateManager(self)
        self._cash_manager = CashManager(self)
        self._square_manager = SquareManager()
        self._dice_rolling_manager = DiceRollingManager()
        self._piece_moving_manager = PieceMovingManager(id, self)
    
    def take_turn(self) -> None:
        self.state_manager.state.take_turn()
    
    def draw_card(self, deck: Deque[Card]) -> None:
        card = deck.popleft()
        card.take_effect(self)
        deck.append(card)
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def state_manager(self) -> StateManager:
        return self._state_manager
    
    @property
    def cash_manager(self) -> CashManager:
        return self._cash_manager
    
    @property
    def square_manager(self) -> SquareManager:
        return self._square_manager
    
    @property
    def dice_rolling_manager(self) -> DiceRollingManager:
        return self._dice_rolling_manager
    
    @property
    def piece_moving_manager(self) -> PieceMovingManager:
        return self._piece_moving_manager