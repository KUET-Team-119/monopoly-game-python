from domain.MonopolyGame import MonopolyGame
from domain.player.Player import Player
from domain.square.Square import Square

class SocialFundSquare(Square):

    def __init__(self, index: int, name: str):
        self._index = index
        self._name = name

    def landed_on(self, player: Player) -> None:
        print('사회기금 카드를 한 장 뽑습니다.')
        social_fund_card_deck = MonopolyGame.social_fund_card_deck
        player.draw_card(social_fund_card_deck)