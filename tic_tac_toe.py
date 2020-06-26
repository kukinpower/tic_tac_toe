class Map:

    def __init__(self, read):
        self.read = read
        self.move = 'X'
        self.rows = None
        self.cols = None
        self.diagonals = None
        self.winners_count = 0
        self.winner = None
        self.coordinates = None
        self.x = None
        self.y = None
        self.flag = 1
        self.place = None
        self.placed = 0
        self.digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def make_rows(self):
        self.rows = [self.read[0:3], self.read[3:6], self.read[6:9]]
        self.cols = [self.read[0] + self.read[3] + self.read[6],
                     self.read[1] + self.read[4] + self.read[7],
                     self.read[2] + self.read[5] + self.read[8]]
        self.diagonals = [self.read[0] + self.read[4] + self.read[8],
                          self.read[2] + self.read[4] + self.read[6]]

    def print_map(self):
        print('-' * 9)
        print(f'| {self.read[0]} {self.read[1]} {self.read[2]} |')
        print(f'| {self.read[3]} {self.read[4]} {self.read[5]} |')
        print(f'| {self.read[6]} {self.read[7]} {self.read[8]} |')
        print('-' * 9)

    def check_winner(self):
        if 'XXX' in self.rows + self.cols + self.diagonals:
            self.winner = 'X wins'
            self.winners_count += 1
        if 'OOO' in self.rows + self.cols + self.diagonals:
            self.winner = 'O wins'
            self.winners_count += 1

    def next_move(self):
        self.x, self.y = [int(n) for n in input("Enter the coordinates:").split()]
        if (not (self.x in self.digits)) or (not (self.y in self.digits)):
            print("You should enter numbers!")
        if not(4 > self.x >= 0 and 4 > self.y >= 0):
            print("Coordinates should be from 1 to 3!")
            return 0
        if self.x == 1:
            if self.y == 3:
                self.place = 0
            elif self.y == 2:
                self.place = 3
            elif self.y == 1:
                self.place = 6
        elif self.x == 2:
            if self.y == 3:
                self.place = 1
            elif self.y == 2:
                self.place = 4
            elif self.y == 1:
                self.place = 7
        elif self.x == 3:
            if self.y == 3:
                self.place = 2
            elif self.y == 2:
                self.place = 5
            elif self.y == 1:
                self.place = 8
        temp = list(self.read)
        if temp[self.place] != 'X' and temp[self.place] != 'O':
            temp[self.place] = self.move
            self.read = ''.join(temp)
            self.placed = 1
        else:
            print("This cell is occupied! Choose another one!")
        return 1

    def change_player(self):
        if self.move == 'X':
            self.move = 'O'
        else:
            self.move = 'X'
        self.placed = 0

    def match(self):
        self.print_map()
        while self.flag:
            while not self.placed:
                self.next_move()
            self.make_rows()
            self.check_winner()
            if self.winner == 'X wins':
                self.print_map()
                print("X wins")
                self.flag = 0
            elif self.winner == 'O wins':
                self.print_map()
                print("O wins")
                self.flag = 0
            elif not (any(i == ' ' for i in self.read)):
                self.print_map()
                print("Draw")
                self.flag = 0
            else:
                self.print_map()
            self.change_player()


game = Map("         ")
game.match()
