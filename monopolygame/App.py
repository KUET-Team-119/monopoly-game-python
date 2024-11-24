from domain.MonopolyGame import MonopolyGame

class App:
    def __init__(self):
        self.monopoly_games = []
        self.current_game = None

    def start_new_game(self):
        print('새로운 게임을 시작합니다.')
        self.current_game = MonopolyGame('1')
        self.monopoly_games.append(self.current_game)

        self.current_game.initialize()

if __name__ == '__main__':
    print('안녕하세요. 모노폴리 게임 시뮬레이터입니다.')
    app = App()
    app.start_new_game()