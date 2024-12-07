from typing import Final, List, Dict, Deque
from collections import deque
from domain.player.Player import Player
from domain.component.Board import Board
from domain.component.card.Card import Card
from domain.component.card.CardType import CardType
from domain.component.card.ChanceCardType import ChanceCardType
from domain.component.card.ChanceCardFactory import ChanceCardFactory
from domain.component.card.SocialFundCardType import SocialFundCardType
from domain.component.card.SocialFundCardFactory import SocialFundCardFactory

import random
import heapq

class MonopolyGame:

    ROUND_TOTAL: Final = 20

    def __init__(self, id: str):
        self._id: str = id
        self._board: Board = Board()
        self._players: Dict[str, Player] = {}
        self._bankrupt_players: Deque[Player] = deque([])
        self._chance_card_deck: Deque[Card] = deque([])
        self._social_fund_card_deck: Deque[Card] = deque([])
    
    def initialize(self) -> None:
        num_of_player = self.enter_num_of_player()
        self.generate_player(num_of_player)
        self.build_deck(ChanceCardType)
        self.build_deck(SocialFundCardType)
        self.shuffle_deck()  # shuffle chance card deck
        self.shuffle_deck()  # shuffle social fund card deck
        self.play_game()
    
    def play_game(self) -> None:
        print('게임 시작!')
        for i in range(MonopolyGame.ROUND_TOTAL):
            self.print_round_number(i)
            try:
                self.play_round()
            except Exception as e:
                print(e)
                break
        self.finish_game()
    
    def print_round_number(self, number: int) -> None:
        if number == MonopolyGame.ROUND_TOTAL:
            print('마지막 라운드를 진행합니다.')
            return
        print(f'제{number}라운드를 진행합니다.')
    
    def play_round(self) -> None:
        for player in self.players.values:
            if player.state_manager.is_bankrupt_state():
                continue
            player.take_turn()
            self.check_remaining_player()

    def enter_num_of_player(self) -> int:
        while True:
            print('플레이어 수를 입력하세요: ')
            num_of_player = int(input())
            if 2 <= num_of_player <= 8:
                return num_of_player
            print('플레이어 수는 2명 이상, 8명 이하여야 합니다.')
    
    def generate_player(self, num_of_player: int) -> None:
        for i in range(num_of_player):
            player_id = str(i)
            self.players[player_id] = Player(player_id)
        
    def build_deck(self, data_type: str, card_types: CardType) -> None:
        if data_type == 'chance_card':
            for card_type in card_types:
                self.chance_card_deck.append(ChanceCardFactory.create_chance_cards(card_type))
        elif data_type == 'social_fund_card':
            for card_type in card_types:
                self.social_fund_card_deck.append(SocialFundCardFactory.create_social_fund_card(card_type))
        else:
            raise ValueError(f'알 수 없는 카드 유형: {data_type}')
    
    def shuffle_deck(self, deck: Deque[Card]) -> None:
        random.shuffle(deck)
    
    def handle_bankrupt_player(self, player: Player) -> None:
        self.bankrupt_players.append(player)
    
    def check_remaining_players(self) -> None:
        if len(self.bankrupt_players) == len(self.players) - 1:
            raise Exception('플레이어가 한 명 남았습니다.')
    
    def finish_game(self) -> None:
        print('게임이 종료되었습니다.')
        self.rank_player()

    def rank_players(self) -> None:
        survived_players_rank = self.rank_survived_players_by_assets()
        bankrupted_players_rank = self.rank_bankrupt_players_by_survival_time()

        self.announce_winner(self.combine_player_rank(survived_players_rank, bankrupted_players_rank))
    
    def rank_survived_players_by_assets(self) -> List:
        survived_players_rank = []

        for player in self.players:
            if not player.state_manager.is_bankrupt_state():
                assets = player.cash_manager.calculate_total_assets()
                heapq.heappush(survived_players_rank, (assets, player))
        
        return survived_players_rank
    
    def rank_bankrupt_players_by_survival_time(self) -> List:
        return list(self.bankrupt_players)
    
    def combine_player_rank(self, survived_players_rank: List[Player], bankrupted_players_rank: List[Player]) -> List:
        return survived_players_rank.extend(bankrupted_players_rank)
    
    def announce_winner(self, rank: List[Player]) -> None:
        print('순위를 공개합니다.')
        for index, player in enumerate(rank):
            print(f'{index + 1}등: 플레이어{player.id}')

    @property
    def chance_card_deck(self):
        return self._chance_card_deck
    
    @property
    def social_fund_card_deck(self):
        return self._social_fund_card_deck