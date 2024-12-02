from domain.square.Square import Square
from domain.square.SquareType import SquareType
from domain.square.LotSquare import LotSquare
from domain.square.RailRoadSquare import RailRoadSquare
from domain.square.UtilitySquare import UtilitySquare
from domain.square.StartSquare import StartSquare
from domain.square.JailSquare import JailSquare
from domain.square.FreeParkingSquare import FreeParkingSquare
from domain.square.GoToJailSquare import GoToJailSquare
from domain.square.IncomeTaxSquare import IncomeTaxSquare
from domain.square.LuxuryTaxSquare import LuxuryTaxSquare
from domain.square.SocialFundSquare import SocialFundSquare
from domain.square.ChanceSquare import ChanceSquare

class SquareFactory:
    index_counter: int = -1

    @classmethod
    def create_square(cls, square_type: SquareType) -> Square:
        cls.index_counter += 1
        index = cls.index_counter

        match square_type:
            case SquareType.LOT_SUWON | SquareType.LOT_YONGIN | SquareType.LOT_GUNSAN | \
                 SquareType.LOT_IKSAN | SquareType.LOT_JEONJU | SquareType.LOT_GYEONGJU | \
                 SquareType.LOT_POHANG | SquareType.LOT_DAEGU | SquareType.LOT_CHANGWON | \
                 SquareType.LOT_ULSAN | SquareType.LOT_BUSAN | SquareType.LOT_JEJU | \
                 SquareType.LOT_YEOSU | SquareType.LOT_GWANGJU | SquareType.LOT_CHUNCHEON | \
                 SquareType.LOT_GANGNEUNG | SquareType.LOT_WONJU | SquareType.LOT_CHEONGJU | \
                 SquareType.LOT_CHEONAN | SquareType.LOT_DAEJEON | SquareType.LOT_INCHEON | \
                 SquareType.LOT_SEOUL:
                return LotSquare(index, square_type.name, square_type.price)
            
            case SquareType.RAILROAD_GWANGJU | SquareType.RAILROAD_BUSAN | \
                 SquareType.RAILROAD_CHUNCHEON | SquareType.RAILROAD_SEOUL:
                return RailRoadSquare(index, square_type.name, square_type.price)
            
            case SquareType.UTILITY_ELECTRIC | SquareType.UTILITY_WATER:
                return UtilitySquare(index, square_type.name, square_type.price)
            
            case SquareType.START:
                return StartSquare(index, square_type.name)
            
            case SquareType.JAIL:
                return JailSquare(index, square_type.name)
            
            case SquareType.FREE_PARKING:
                return FreeParkingSquare(index, square_type.name)
            
            case SquareType.GO_TO_JAIL:
                return GoToJailSquare(index, square_type.name)
            
            case SquareType.INCOME_TAX:
                return IncomeTaxSquare(index, square_type.name)
            
            case SquareType.LUXURY_TAX:
                return LuxuryTaxSquare(index, square_type.name)
            
            case SquareType.SOCIAL_FUND_2 | SquareType.SOCIAL_FUND_17 | SquareType.SOCIAL_FUND_33:
                return SocialFundSquare(index, square_type.name)
            
            case SquareType.CHANCE_7 | SquareType.CHANCE_22 | SquareType.CHANCE_36:
                return ChanceSquare(index, square_type.name)
            
            case _:
                raise ValueError(f'알 수 없는 부지 유형: {square_type}')