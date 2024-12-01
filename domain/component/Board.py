from typing import Final, Dict
from domain.square import Square, SquareFactory, SquareType


class Board:
    SQUARES_TOTAL: Final = 40
    MAX_COUNT_OF_HOUSE_ON_BOARD: Final = 32
    MAX_COUNT_OF_HOTEL_ON_BOARD: Final = 12

    squares: Dict[int, Square]
    current_count_of_house: int
    current_count_of_hotel: int

    def __init__(self):
        Board.squares = {}
        Board.current_count_of_house = 0
        Board.current_count_of_hotel = 0
        Board.create_square()

    @classmethod
    def can_build_house(cls) -> bool:
        return cls.current_count_of_house < cls.MAX_COUNT_OF_HOUSE_ON_BOARD

    @classmethod
    def can_build_hotel(cls) -> bool:
        return cls.current_count_of_hotel < cls.MAX_COUNT_OF_HOTEL_ON_BOARD

    @classmethod
    def add_count_of_house(cls):
        cls.current_count_of_house += 1

    @classmethod
    def add_count_of_hotel(cls):
        cls.current_count_of_hotel += 1
    
    @classmethod
    def create_square(cls):
        for square_type in SquareType:
            cls.squares[square_type.index] = SquareFactory.create_square(square_type)