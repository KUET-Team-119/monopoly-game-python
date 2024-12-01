from typing import Final
from domain.component.Cup import Cup

class DiceRollingManager:
    MAX_COUNT_OF_DOUBLE: Final = 3

    def __init__(self):
        self._cup = Cup.INSTANCE

    def roll_dice(self) -> int:
        print('주사위를 굴립니다.')
        return self._cup.roll()

    def is_double(self) -> bool:
        return self._cup.is_double()