import random
from os import name, system

from art import logo, vs
from game_data import data

score = 0

def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')
def random_data():
    return random.choice(data)

def new_compare():

    print(logo)
    a = random_data()
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    b = random_data()
    if a == b:
        b = random_data()
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    print("Who has more followers? Type 'A' or 'B': ")
    user_choice = input().lower()

    while user_choice == 'a' or user_choice == 'b':
        global score

        if (user_choice == 'a' and a['follower_count'] > b['follower_count']) or (user_choice == 'b' and b['follower_count'] > a['follower_count']):
            score += 1
            correct_answer = True
            print(f"You're right! Current score: {score}")

            new_compare()
            break

        else:
            correct_answer = False

            print(f"Sorry, that's wrong. Final score: {score}")
            break
new_compare()

# Clear screen / console didn't work for some reason, to investigate
