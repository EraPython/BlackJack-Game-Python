import random
from art import logo

def deal_cards():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"
    if computer_score == user_score:
        return "Draw"
    elif computer_score == 0:
        return "You loose, your opponent has a blackjack"
    elif user_score == 0:
        return "Win with a blackjack!"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Your opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get an another card, 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_cards != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(computer_score=computer_score, user_score=user_score))

while input("Wanna play the game? Press 'y' to play, 'n' to not: ") == "y":
    play_game()