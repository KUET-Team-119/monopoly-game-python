from domain.player.PlayerState.PlayerState import PlayerState
from domain.player.Player import Player

class PrisonState(PlayerState):
    BAIL_AMOUNT: int = 50  # 보석금
    INITIAL_PRISON_TERM: int = 3  # 초기 수감 기간
    
    def __init__(self, player: Player):
        self._player = player
        self._prison_term = self.INITIAL_PRISON_TERM

    def take_turn(self) -> None:
        if self._prison_term > 0:
            self._prison_term -= 1
            print(f'남은 수감 기간: {self._prison_term}')

            if self._prison_term == 0:
                self._player.get_cash_manager().reduce_cash(self.BAIL_AMOUNT)
                self._pay_bail_and_exit()
            else:
                self._attempt_prison_escape()

    def _attempt_prison_escape(self) -> None:
        print('더블을 굴려 탈옥을 시도합니다.')
        roll_result = self._player.get_dice_rolling_manager().roll_dice()

        if self._player.get_dice_rolling_manager().is_double():
            print('더블이 나왔습니다. 탈옥에 성공했습니다!')
            self._leave_jail_and_move(roll_result)
        else:
            print('더블이 나오지 않았습니다.')
            print('다음 턴까지 감옥에 남습니다.')

    def _pay_bail_and_exit(self) -> None:
        paid_cash = self._player.get_cash_manager().reduce_cash(self.BAIL_AMOUNT)
        if paid_cash == self.BAIL_AMOUNT:
            self._leave_jail()
            self._player.take_turn()  # 정상 상태에서 턴 실행

    def _leave_jail_and_move(self, steps: int) -> None:
        self._leave_jail()
        self._player.get_piece_moving_manager().move_forward_by_steps(steps)

    def _leave_jail(self) -> None:
        self._player.get_state_manager().become_normal_state()  # 정상 상태로 복귀
        print('감옥에서 나옵니다.')