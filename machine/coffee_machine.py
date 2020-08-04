
class CoffeeMachine:
    choice = ""
    coffee = ""

    def __init__(self):
        self.items = {'water': {'1': 250, '2': 350, '3': 200, 'have': 400, 'add': 0},
                      'milk': {'1': 0, '2': 75, '3': 100, 'have': 540, 'add': 0},
                      'beans': {'1': 16, '2': 20, '3': 12, 'have': 120, 'add': 0},
                      'cups': {'1': 1, '2': 1, '3': 1, 'have': 9, 'add': 0},
                      'money': {'1': 4, '2': 7, '3': 6, 'have': 550}}
        self.machine_options()

    def remaining(self):
        print("\nThe coffee machine has:")
        print(f"{self.items['water']['have']} of water\n"
              f"{self.items['milk']['have']} of milk\n"
              f"{self.items['beans']['have']} of coffee beans\n"
              f"{self.items['cups']['have']} of disposable cups\n"
              f"${self.items['money']['have']} of money\n")

    def machine_options(self):
        while True:
            self.choice = input("Write action (buy, fill, take, remaining, exit):\n")
            if self.choice == "buy":
                self.coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
                if self.coffee == "back":
                    continue
                self.coffee_options()
            elif self.choice == "fill":
                self.items['water']['add'] = int(input("Write how many ml of water do you want to add:\n"))
                self.items['milk']['add'] = int(input("Write how many ml of milk do you want to add:\n"))
                self.items['beans']['add'] = int(input("Write how many grams of coffee beans do you want to add:\n"))
                self.items['cups']['add'] = int(input("Write how many disposable cups of coffee do you want to add:\n"))
                self.fill_option()
            elif self.choice == "take":
                self.take_option()
            elif self.choice == "remaining":
                self.remaining()
            else:
                exit()

    def coffee_options(self):
        if self.items['water']['have'] < self.items['water'][self.coffee]:
            print("Sorry, not enough water!")
        elif self.items['milk']['have'] < self.items['milk'][self.coffee]:
            print("Sorry, not enough milk!")
        elif self.items['beans']['have'] < self.items['beans'][self.coffee]:
            print("Sorry, not enough coffee beans!")
        elif self.items['cups']['have'] < self.items['cups'][self.coffee]:
            print("Sorry, not enough disposable cups!")
        else:
            self.items['water']['have'] -= self.items['water'][self.coffee]
            self.items['milk']['have'] -= self.items['milk'][self.coffee]
            self.items['beans']['have'] -= self.items['beans'][self.coffee]
            self.items['cups']['have'] -= self.items['cups'][self.coffee]
            self.items['money']['have'] += self.items['money'][self.coffee]
            print("I have enough resources. making you a coffee!")

    def fill_option(self):
        self.items['water']['have'] += self.items['water']['add']
        self.items['milk']['have'] += self.items['milk']['add']
        self.items['beans']['have'] += self.items['beans']['add']
        self.items['cups']['have'] += self.items['cups']['add']

    def take_option(self):
        print(f"I gave you ${self.items['money']['have']}\n")
        self.items['money']['have'] = 0


if __name__ == "__main__":
    CoffeeMachine()
