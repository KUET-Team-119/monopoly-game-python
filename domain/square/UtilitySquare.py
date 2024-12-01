from domain.square.PropertySquare import PropertySquare

class UtilitySquare(PropertySquare):
    
    def __init__(self, index: int, name: str, price: int):
        super().__init__(index, name, price)
    
    def rent(self) -> int:
        count: int = self._owner.square_manager.count_utility_squares()
        face_value: int = self._owner.dice_rolling_manager.roll_dice()
        if count == 1:
            return face_value * 4
        return face_value * 10
    
    def manage_square(self) -> None:
        print(f'{self._name}을 둘러봅니다.')