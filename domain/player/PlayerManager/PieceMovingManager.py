from domain.component.Piece import Piece
from domain.player.Player import Player
from domain.square.SquareType import SquareType

class PieceMovingManager:
    def __init__(self, id: str, player: Player):
        self._piece = Piece(id, player)

    # 말을 몇 칸 앞으로 이동시키는 행동
    def move_forward_by_steps(self, steps: int) -> None:
        self._piece.move_forward_by_steps(steps)

    # 말을 몇 칸 뒤로 이동시키는 행동
    def move_backward_by_steps(self, steps: int) -> None:
        self._piece.move_backward_by_steps(steps)

    # 말을 특정 칸까지 앞으로 이동시키는 행동
    def move_forward_to_square_type(self, destination: SquareType) -> None:
        self._piece.move_forward_to_square_type(destination)

    # 말을 특정 칸으로 순간이동시키는 행동
    def warp_to_square_type(self, destination: SquareType) -> None:
        self._piece.set_location(destination)

    def get_current_location_id(self) -> int:
        return self._piece.get_location_id()