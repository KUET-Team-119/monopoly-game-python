from domain.player.PlayerState.PlayerState import PlayerState
from domain.player.Player import Player

class NormalState(PlayerState):

    def __init__(self, player: Player):
        self._player = player
    
    def take_turn(self) -> None:
        print(f'플레이어 {self._player.id}의 차례입니다.')

        count_of_double = 0
        while self._player.state_manager.is_normal_state():
            steps = self._player.dice_rolling_manager.roll_dice()
            print(f'주사위 결과: {steps}')

            if self._player.dice_rolling_manager.is_double():
                print('더블입니다.')
                if (count_of_double := count_of_double + 1) == self._player.dice_rolling_manager.MAX_COUNT_OF_DOUBLE:
                    self.send_to_prison()
                    break
                self.move_player(steps)
            else:
                self.move_player(steps)
                break
    
    def send_to_prison(self) -> None:
        print(f'더블이 연속 {self._player.dice_rolling_manager.MAX_COUNT_OF_DOUBLE}회 나왔습니다. 감옥으로 갑니다.')
        self._player.state_manager.become_prison_state()
    
    def move_player(self, steps: int) -> None:
        self._player.piece_moving_manager.move_forward_by_steps(steps)