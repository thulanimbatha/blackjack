# Project
import random

# Ace to King : Ace counts as 11, face cards count as 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
comp_cards = []
user_cards.append(random.choice(cards))
user_cards.append(random.choice(cards))
comp_cards.append(random.choice(cards))
comp_cards.append(random.choice(cards))
print(f"Your cards: {user_cards}\nComputer cards: {comp_cards}")
while sum(user_cards) <= 21 and sum(comp_cards) <= 21:
    if input("Hit? (type 'y' to hit 'n' to not hit): ") == 'y':
        user_cards.append(random.choice(cards))
    print(f"Your cards: {user_cards}\nComputer cards: {comp_cards}")


if sum(user_cards) > 21:
    print("You lose!")
elif sum(comp_cards) > 21:
    print("You win")
