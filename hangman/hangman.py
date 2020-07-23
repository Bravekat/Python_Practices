import random


class Hangman:
    def __init__(self):
        self.answers = ['python', 'java', 'kotlin', 'javascript']
        self.answer = random.choice(self.answers)
        self.display = ["-" for _ in self.answer]
        self.lives = 8
        self.guess = ""
        self.result()

    def check_answer(self):
        if self.guess in self.answer:
            return True
        print("No such letter in the word\n")
        self.lives -= 1
        self.check()

    def check_display(self):
        if self.guess is not self.display:
            return True
        print("You already typed this letter")
        self.check()

    def check_lower(self):
        if self.guess.lower() == self.guess:
            return True
        print("It is not an ASCII lowercase letter")
        self.check()

    def check_length(self):
        if len(self.guess) == 1:
            return True
        print("You should input a single letter")
        self.check()

    def check(self):
        while self.lives == 0 or '-' not in self.display:
            print("".join(self.display))
            self.guess = input("Input a letter: ")
            if self.check_lower() and self.check_answer() and self.check_display() and self.check_length():
                for i in range(0, len(self.answer)):
                    if self.guess == self.answer[i]:
                        self.display[i] = self.guess
                        print()
        if self.lives == 0:
            print("You are hanged!")
        else:
            print(f"{''.join(self.display)}\nYou guessed the word!\nYou survived!")

    def result(self):
        print("H A N G M A N\n")
        n = input('Type "play" to play the game, "exit" to quit: ')
        if n == "play":
            self.check()
        else:
            exit()


if __name__ == "__main__":
    Hangman()
