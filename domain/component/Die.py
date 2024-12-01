import random

class Die:
    def __init__(self):
        self._face_value: int = 1  # 초기값 설정

    def roll(self) -> None:
        self._face_value = random.randint(1, 6)
        print(f'주사위의 눈: {self._face_value}')

    @property
    def face_value(self) -> int:
        return self._face_value
