# Project
import random

def deal_card():
    '''Returns a random card from deck'''
    # Ace to King : Ace counts as 11 or 1, face cards count as 10
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards_list):
    '''Returns sum of cards_list'''
    # check for a blackjack (ace + 11 cards) - return 0 if true
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0

    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)

    return sum(cards_list)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "draw"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over, you lose"
    elif comp_score > 21:
        return "Opponent went over, you win"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards = []
    comp_cards = []
    is_game_over = False
    # for-loop to run twice
    # deal 2 cards each for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    # user turn
    while not is_game_over:

        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # computer turn: as long as score is less than 17
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"Your final hand: {user_cards} . Final score: {user_score}")
    print(f"Comp final hand: {comp_cards} . Final score: {comp_score}")
    print(compare(user_score, comp_score))

# GAME START
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()