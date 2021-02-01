# Import and def
import random


def lose(op):
    print(f"Sorry, but the computer chose {op}")


def draw(op):
    print(f'There is a draw ({op})')


def win(op):
    print(f"Well done. The computer chose {op} and failed")


# variable
chose = ['rock', 'paper', 'scissors', ]
game = True

while game:
    user_option = input()
    computer_option = random.choice(chose)

    if user_option == '!exit':
        print("!bye")
        game = False
        break
    elif user_option != chose[0] and user_option != chose[1] and user_option != chose[2]:
        print("Invalid input")
    elif user_option == computer_option:
        draw(computer_option)
    elif user_option == chose[0] and computer_option == chose[2]:
        win(computer_option)
    elif user_option == chose[2] and computer_option == chose[1]:
        win(computer_option)
    elif user_option == chose[1] and computer_option == chose[0]:
        win(computer_option)
    else:
        lose(computer_option)
