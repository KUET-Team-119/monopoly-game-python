from domain.MonopolyGame import MonopolyGame

class App:
    def __init__(self):
        self._monopoly_games = []
        self._current_game = None

    def start_new_game(self) -> None:
        print('새로운 게임을 시작합니다.')
        self._current_game = MonopolyGame('1')
        self._monopoly_games.append(self.current_game)

        self._current_game.initialize()

if __name__ == '__main__':
    print('안녕하세요. 모노폴리 게임 시뮬레이터입니다.')
    app = App()
    app.start_new_game()