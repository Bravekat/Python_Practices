import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS card ("
            "id INTEGER, number TEXT, pin TEXT, balance INTEGER default 0 "
            ")")
conn.commit()


def menu():
    while True:
        print("1. Create an account\n2. Log into account\n0. Exit")
        command = int(input())
        if command == 1:
            create_acount()
        elif command == 2:
            if login() == 0:
                print("Bye!")
                return
        elif command == 0:
            print("Bye!")
            return


def create_acount():
    bank_ident_num = "400000"
    account_ident = "{:09}".format(random.randint(0, 999999999))
    checksum = calc_checksum(bank_ident_num + account_ident)
    card_number = bank_ident_num + account_ident + checksum
    pin = "{:04}".format(random.randint(0, 9999))
    cur.execute("SELECT * FROM card")
    cur.execute("INSERT INTO card VALUES (?,?,?,?)", (len(cur.fetchall())+1, card_number, pin, 0))
    conn.commit()
    print("Your card has been created\nYour card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin)
    return


def calc_checksum(number):
    checksum = 0
    i = 1
    digits = list(number)
    for digit in digits:
        checksum += (int(digit) * 2 if int(digit) * 2 < 10 else int(digit) * 2 - 9) if i % 2 else int(digit)
        i += 1
    return str(10 - checksum % 10)[-1]


def login():
    print("Enter your card number:")
    card_number = input()
    print("Enter your PIN:")
    pin = input()
    cur.execute("SELECT * FROM card WHERE number = ?", (card_number,))
    account = cur.fetchone()
    if account:
        if account[2] == pin:
            print("You have successfully logged in!")
            while True:
                print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
                command = int(input())
                if command == 1:
                    print("Balance:", account[3])
                elif command == 2:
                    add_ = int(input("Enter income:\n"))
                    cur.execute(f"UPDATE card SET balance = balance + {add_} WHERE number = ?", (card_number,))
                    cur.execute("SELECT * FROM card WHERE number = ?", (card_number,))
                    account = cur.fetchone()
                    conn.commit()
                    print("Income was added!")
                elif command == 3:
                    cur.execute("SELECT number FROM card")
                    card_ = input("Enter card number:\n")
                    check_ = [i[0] for i in cur.fetchall()]
                    if calc_checksum(card_) != '0':
                        print("Probably you made mistake in the card number. Please try again!")
                        continue
                    for i in check_:
                        if i == card_:
                            cur.execute("SELECT * FROM card WHERE number = ?", (i,))
                            amount_ = int(input("Enter how much money you want to transfer:\n"))
                            if amount_ > account[3]:
                                print("Not enough money!")
                                continue
                            else:
                                cur.execute(f"UPDATE card SET balance = balance - {amount_} WHERE number = ?", (card_number,))
                                cur.execute(f"UPDATE card SET balance = balance + {amount_} WHERE number = ?", (card_,))
                                conn.commit()
                                print("Success!")
                                continue
                    print("Such a card does not exist.")
                elif command == 4:
                    cur.execute("DELETE FROM card WHERE number = ?", (card_number,))
                    conn.commit()
                    print("The account has been closed")
                elif command == 5:
                    print("You have successfully logged out!")
                    return
                elif command == 0:
                    return 0
        else:
            print("Wrong card number or PIN!")
    else:
        print("Wrong card number or PIN!")


menu()
