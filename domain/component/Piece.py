from domain.player.Player import Player
from domain.square.Square import Square
from domain.square.SquareType import SquareType
from domain.component.Board import Board

class Piece:
    def __init__(self, id: str, player: Player):
        self._id: str = id
        self._player: Player = player
        self._location: Square = Board.squares[SquareType.START.index]  # 출발점에서 시작

    # 몇 칸 앞으로 이동하는 행동
    def move_forward_by_steps(self, steps: int) -> None:
        print(f"앞으로 {steps}칸 이동합니다.")
        current_location_id = self.get_location_id()
        destination_id = (current_location_id + steps) % Board.SQUARES_TOTAL
        
        if self._is_passed_go_square(destination_id, current_location_id):
            print("출발칸을 지나갔으니 월급 받으세요.")
            self._player.cash_manager.add_cash(200)
            
        self.set_location(Board.squares[destination_id])

    # 몇 칸 뒤로 이동하는 행동
    def move_backward_by_steps(self, steps: int) -> None:
        print(f"뒤로 {steps}칸 이동합니다.")
        current_location_id = self.get_location_id()
        
        if current_location_id >= steps:
            self.set_location(Board.squares[self.get_location_id() - steps])
        else:
            self.set_location(Board.squares[Board.SQUARES_TOTAL + current_location_id - steps])

    # 특정 칸까지 앞으로 이동하는 행동
    def move_forward_to_square_type(self, square_type: SquareType) -> None:
        destination_id = square_type.index
        current_location_id = self.get_location_id()
        
        if destination_id >= current_location_id:
            self.move_forward_by_steps(destination_id - current_location_id)
        else:
            self.move_forward_by_steps(Board.SQUARES_TOTAL - self.get_location_id() + square_type.index)

    # 인자로 받은 SquareType으로 말의 위치 변경
    def set_location(self, destination: SquareType | Square) -> None:
        if isinstance(destination, SquareType):
            self._location = Board.squares[destination.index]
        else:
            self._location = destination
            
        print(f"{self._location.name}에 도착했습니다.")
        self._location.landed_on(self._player)

    def _is_passed_go_square(self, current_location_id: int, destination_id: int) -> bool:
        return destination_id < current_location_id and destination_id != SquareType.START.index

    def get_location_id(self) -> int:
        return self._location.index