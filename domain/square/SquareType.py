from enum import Enum

class SquareType(Enum):
    START = (0, '출발점', 0)
    LOT_SUWON = (1, '수원', 60)
    SOCIAL_FUND_2 = (2, '사회사업기금', 0)
    LOT_YONGIN = (3, '용인', 60)
    INCOME_TAX = (4, '소득세', 0)
    RAILROAD_GWANGJU = (5, '광주역', 200)
    LOT_GUNSAN = (6, '군산', 100)
    CHANCE_7 = (7, '찬스', 0)
    LOT_IKSAN = (8, '익산', 100)
    LOT_JEONJU = (9, '전주', 120)
    JAIL = (10, '감옥', 0)
    LOT_GYEONGJU = (11, '경주', 140)
    UTILITY_ELECTRIC = (12, '전력공사', 150)
    LOT_POHANG = (13, '포항', 140)
    LOT_DAEGU = (14, '대구', 160)
    RAILROAD_BUSAN = (15, '부산역', 200)
    LOT_CHANGWON = (16, '창원', 180)
    SOCIAL_FUND_17 = (17, '사회사업기금', 0)
    LOT_ULSAN = (18, '울산', 180)
    LOT_BUSAN = (19, '부산', 200)
    FREE_PARKING = (20, '무료 주차장', 0)
    LOT_JEJU = (21, '제주', 220)
    CHANCE_22 = (22, '찬스', 0)
    LOT_YEOSU = (23, '여수', 220)
    LOT_GWANGJU = (24, '광주', 240)
    RAILROAD_CHUNCHEON = (25, '춘천역', 200)
    LOT_CHUNCHEON = (26, '춘천', 260)
    LOT_GANGNEUNG = (27, '강릉', 260)
    UTILITY_WATER = (28, '수자원공사', 150)
    LOT_WONJU = (29, '원주', 280)
    GO_TO_JAIL = (30, '감옥으로 가시오', 0)
    LOT_CHEONGJU = (31, '청주', 300)
    LOT_CHEONAN = (32, '천안', 300)
    SOCIAL_FUND_33 = (33, '사회사업기금', 0)
    LOT_DAEJEON = (34, '대전', 320)
    RAILROAD_SEOUL = (35, '서울역', 200)
    CHANCE_36 = (36, '찬스', 0)
    LOT_INCHEON = (37, '인천', 350)
    LUXURY_TAX = (38, '사치세', 0)
    LOT_SEOUL = (39, '서울', 400)

    def __init__(self, index: int, name: str, price: int):
        self._index = index
        self._name = name
        self._price = price
    
    @property
    def index(self) -> int:
        return self._index
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> int:
        return self._price