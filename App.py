from domain.MonopolyGame import MonopolyGame

class App:
    _monopoly_games = []
    _current_game = None

    @classmethod
    def start_new_game(cls) -> None:
        print('새로운 게임을 시작합니다.')
        cls._current_game = MonopolyGame(str(len(cls._monopoly_games) + 1))
        cls._monopoly_games.append(cls._current_game)

        cls._current_game.initialize()

    @classmethod
    def display_menu(cls) -> None:
        print('안녕하세요. 모노폴리 게임 시뮬레이터입니다.')
        print('===== 모노폴리 게임 메뉴 =====')
        print('1. 새로운 게임 시작')
        print('2. 종료')
        print('=============================')

    @classmethod
    def run(cls) -> None:
        while True:
            cls.display_menu()
            choice = input('메뉴를 선택하세요 (1 또는 2): ').strip()
            match choice:
                case '1':
                    cls.start_new_game()
                case '2':
                    print('모노폴리 게임 시뮬레이터를 종료합니다.')
                    break
                case _:
                    print('잘못된 입력입니다. 다시 시도하세요.')

if __name__ == '__main__':
    App.run()