class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def display_board(self):
        print('---------')
        for i in range(0, 9, 3):
            print('|', self.board[i], '|', self.board[i+1], '|', self.board[i+2], '|')
            print('---------')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Попробуйте ещё раз')

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return self.board[combination[0]]
        if ' ' not in self.board:
            return 'Ничья'
        return None

    def play(self):
        while True:
            self.display_board()
            position = int(input('Введите позицию(0-8): '))
            self.make_move(position)
            winner = self.check_winner()
            if winner:
                self.display_board()
                if winner == 'Ничья':
                    print('Это ничья')
                else:
                    print(f'{winner} победил!')
                break

# Создаем экземпляр игры и запускаем игру
game = TicTacToe()
game.play()