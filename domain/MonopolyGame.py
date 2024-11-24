from typing import Final, List, Deque
from collections import deque
import random
import heapq

ROUND_TOTAL: Final = 20

class MonopolyGame:
    def __init__(self, id: str):
        self.id = id
        self.board = Board()
        self.players = {}
        self.bankrupt_players = deque([])
        self.chance_card_deck = deque([])
        self.social_fundCard_deck = deque([])
    
    def initialize(self):
        num_of_player = self.enter_num_of_player()
        self.generate_player(num_of_player)
        self.build_deck()    # build chance card deck
        self.build_deck()    # build social fund card deck
        self.shuffle_deck()  # shuffle chance card deck
        self.shuffle_deck()  # shuffle social fund card deck
        self.play_game()
    
    def play_game(self):
        print('게임 시작!')
        for i in range(ROUND_TOTAL):
            self.print_round_number(i)
            try:
                self.play_round()
            except Exception as e:
                print(e)
                break
        self.finish_game()
    
    def print_round_number(self, number: int):
        if number == ROUND_TOTAL:
            print('마지막 라운드를 진행합니다.')
            return
        print(f'제{number}라운드를 진행합니다.')
    
    def play_round(self):
        for player in self.players.values:
            if player.state_manager.is_bankrupt_state():
                continue
            player.take_turn()
            self.check_remaining_player()

    def enter_num_of_player(self):
        while True:
            print('플레이어 수를 입력하세요: ')
            num_of_player = int(input())
            if 2 <= num_of_player <= 8:
                return num_of_player
            print('플레이어 수는 2명 이상, 8명 이하여야 합니다.')
    
    def generate_player(self, num_of_player: int):
        for i in range(num_of_player):
            player_id = str(i)
            self.players[player_id] = Player(player_id)
    
    def build_deck(self, types: List[SocialFundCardType]):
        for type in types:
            self.chance_card_deck.append(SocialFundCardFactory.create_social_fund_cards(type))
    
    def shuffle_deck(self, deck: Deque[Card]):
        random.shuffle(deck)
    
    def handle_bankrupt_player(self, player: Player):
        self.bankrupt_players.append(player)
    
    def check_remaining_players(self):
        if len(self.bankrupt_players) == len(self.players) - 1:
            raise Exception('플레이어가 한 명 남았습니다.')
    
    def finish_game(self):
        print('게임이 종료되었습니다.')
        self.rank_player()

    def rank_players(self):
        survived_players_rank = self.rank_survived_players_by_assets()
        bankrupted_players_rank = self.rank_bankrupt_players_by_survival_time()

        self.announce_winner(self.combine_player_rank(survived_players_rank, bankrupted_players_rank))
    
    def rank_survived_players_by_assets(self):
        survived_players_rank = []

        for player in self.players:
            if not player.state_manager.is_bankrupt_state():
                assets = player.cash_manager.calculate_total_assets()
                heapq.heappush(survived_players_rank, (assets, player))
        
        return survived_players_rank
    
    def rank_bankrupt_players_by_survival_time(self):
        return list(self.bankrupt_players)
    
    def combine_player_rank(self, survived_players_rank: List[Player], bankrupted_players_rank: List[Player]):
        return survived_players_rank.extend(bankrupted_players_rank)
    
    def announce_winner(self, rank: List[Player]):
        print('순위를 공개합니다.')
        for index, player in enumerate(rank):
            print(f'{index + 1}등: 플레이어{player.get_id()}')