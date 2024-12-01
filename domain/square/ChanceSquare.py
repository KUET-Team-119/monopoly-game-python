from domain.MonopolyGame import MonopolyGame
from domain.player.Player import Player
from domain.square.Square import Square

class ChanceSquare(Square):

    def __init__(self, index: int, name: str):
        self._index = index
        self._name = name
    
    def landed_on(self, player: Player) -> None:
        print('찬스 카드를 한 장 뽑습니다.')
        chance_card_deck = MonopolyGame.chance_card_deck
        player.draw_card(chance_card_deck)