class TicTac:

    def __init__(self):
        self.user_input = None
        self.user_move = None
        self.combinations = None
        self.count_x = 0
        self.count_o = 0
        self.count_under = 0
        self.x_win = 0
        self.o_win = 0
        self.turns = 0
        self.turn = True
        self.matrix = []
        self.grid()
        self.print_result()
        self.user_input_check()

    def grid(self):
        self.user_input = [" " for _ in range(0, 9)]
        for i in range(3):
            self.matrix.append([])
            for j in range(0, 3):
                self.matrix[i].append(self.user_input[0])
                if self.user_input[0] == "X":
                    self.count_x += 1
                elif self.user_input[0] == "O":
                    self.count_o += 1
                elif self.user_input[0] == " ":
                    self.count_under += 1
                else:
                    print("Invalid input")
                    exit()
                self.user_input.pop(0)

    def win_condition(self):
        self.combinations = [[self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]],  # Diagonal [0]
                             [self.matrix[0][2], self.matrix[1][1], self.matrix[2][0]],  # Diagonal [1]
                             [self.matrix[0][0], self.matrix[1][0], self.matrix[2][0]],  # Vertical [2]
                             [self.matrix[0][1], self.matrix[1][1], self.matrix[2][1]],  # Vertical [3]
                             [self.matrix[0][2], self.matrix[1][2], self.matrix[2][2]],  # Vertical [4]
                             [self.matrix[0][0], self.matrix[0][1], self.matrix[0][2]],  # Horizontal [5]
                             [self.matrix[1][0], self.matrix[1][1], self.matrix[1][2]],  # Horizontal [6]
                             [self.matrix[2][0], self.matrix[2][1], self.matrix[2][2]]]  # Horizontal [7]
        self.check()

    def check(self):
        for i in range(8):
            if [self.combinations[i][0], self.combinations[i][1], self.combinations[i][2]] == ["X", "X", "X"]:
                self.x_win += 1
            if [self.combinations[i][0], self.combinations[i][1], self.combinations[i][2]] == ["O", "O", "O"]:
                self.o_win += 1
        self.result()

    def print_result(self):
        print(f"""---------
        | {self.matrix[0][0]} {self.matrix[0][1]} {self.matrix[0][2]} |
        | {self.matrix[1][0]} {self.matrix[1][1]} {self.matrix[1][2]} |
        | {self.matrix[2][0]} {self.matrix[2][1]} {self.matrix[2][2]} |
        ---------""")

    def user_input_check(self):
        while True:
            value = input("Enter the coordinates: ").split()
            if [el for el in value if not el.isnumeric()]:
                print("You should enter numbers!")
            elif [el for el in value if el not in ("1", "2", "3")]:
                print("Coordinates should be from 1 to 3!")
            elif self.matrix[abs(int(value[1]) - 3)][int(value[0]) - 1] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                if self.turn:
                    self.matrix[abs(int(value[1]) - 3)][int(value[0]) - 1] = "X"
                    self.print_result()
                    self.turn = False
                    self.turns += 1
                else:
                    self.matrix[abs(int(value[1]) - 3)][int(value[0]) - 1] = "O"
                    self.print_result()
                    self.turn = True
                    self.turns += 1
                self.win_condition()

    def result(self):
        if (self.x_win > 1 or self.o_win > 1) or (abs(self.count_x - self.count_o) > 1)\
                or (self.x_win and self.o_win > 0):
            print("Impossible")
        elif self.x_win == 1:
            print("X wins")
            exit()
        elif self.o_win == 1:
            print("O wins")
            exit()
        elif self.turns == 9:
            print("Draw")
            exit()
        else:
            self.user_input_check()


if __name__ == "__main__":
    TicTac()
