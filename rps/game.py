import random


class RockPaperScissors:
    def __init__(self):
        self.file_data = {}
        self.user = input('Enter your name: ')
        self.guess = ""
        print(f'Hello, {self.user}')
        self.options = ['rock', 'paper', 'scissors']
        self.set_options()
        print("Okay, let's start")
        self.score = 0
        self.user_setup()
        self.start()

    def set_options(self):
        txt = input()
        if txt:
            self.options = txt.split(',')

    def load_scores(self):
        with open('rating.txt', 'r') as file_:
            for line in file_:
                (key, val) = line.split()
                self.file_data[key] = int(val)
        file_.close()

    def compare(self):
        move = (self.options.index(self.guess) - (len(self.options) - 1) // 2) % len(self.options)
        options = self.options[move:] + self.options[:move]
        cpu = random.choice(options)
        if self.guess == cpu:
            print(f'There is a draw ({cpu})')
            self.score += 50
        if options.index(self.guess) > options.index(cpu):
            print(f'Well done. Computer chose {cpu} and failed')
            self.score += 100
        if options.index(self.guess) < options.index(cpu):
            print(f'Sorry, but computer chose {cpu}')

    def user_setup(self):
        if self.file_data.get(self.user) is None:
            self.file_data.update({self.user: self.score})
        else:
            self.score = self.file_data[self.user]

    def start(self):
        while True:
            self.guess = input()
            if self.guess == '!exit':
                print('Bye!')
                exit()
            if self.guess == '!rating':
                print(f'Your rating: {self.file_data[self.user]}')
            elif self.guess not in self.options:
                print('Invalid input')
            else:
                self.compare()
                self.file_data[self.user] = self.score


if __name__ == "__main__":
    RockPaperScissors()
