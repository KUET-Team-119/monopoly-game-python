from abc import ABC, abstractmethod
from domain.component.Board import Board
from domain.player.Player import Player

class ForwardToNearestChanceCard(ABC):
    def __init__(self, index: int, name: str):
        self.index = index
        self.name = name

    @abstractmethod
    def get_target_square_class(self):
        pass

    def take_effect(self, player: Player):
        current_location_id = player.piece_moving_manager.get_current_location_id()
        target_square = self.get_target_square_class()
        
        board_size = len(Board.squares)
        steps = 0

        for i in range(1, board_size + 1):
            next_location_id = (current_location_id + i) % board_size
            square = Board.squares[next_location_id]
            
            if isinstance(square, target_square):
                steps = i
                break

        if steps > 0:
            player.piece_moving_manager().move_forward_by_steps(steps)
