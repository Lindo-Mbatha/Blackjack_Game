from Logo import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards2 = [5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11]
cards3 = [7, 7, 8, 8, 9, 9]

user_score = 0
dealer_score = 0

question = input("Do you want to play some Blackjack? Y or N? ").lower()

if question == "y":

    answer1_dealer = random.choice(cards2)
    answer2_dealer = random.choice(cards2)
    answer3_dealer = random.choice(cards3)
    answer1_user = random.choice(cards)
    answer2_user = random.choice(cards)

    user_score1 = user_score + answer1_user + answer2_user
    dealer_score1 = dealer_score + answer1_dealer

    print(f"Your cards: [{answer1_user}, {answer2_user}]")
    print(f"Dealer's first card: [{answer1_dealer}]")
    print(f"Your score: {user_score1}")
    print(f"The Dealer's score: {dealer_score1}")

    x = " "
    print(x)

    question2 = input("Do you want another card? Y or N? ").lower()

    if question2 == "y":

        answer3_user = random.choice(cards)
        answer2_dealer = random.choice(cards)

        user_score1 = user_score + answer1_user + answer2_user
        user_score2 = user_score1 + answer3_user
        dealer_score1 = dealer_score + answer1_dealer

        print(f"Your cards: [{answer1_user}, {answer2_user}, {answer3_user}]")
        print(f"Dealer's first card: [{answer1_dealer}]")
        print(f"Your score: {user_score2}")
        print(f"The Dealer's score: {dealer_score1}")

        if user_score2 > 21:
            print(x)
            print("You Lose")
            print(f"Your final cards: [{answer1_user}, {answer2_user}, {answer3_user}]")
            print(f"Dealer's cards: [{answer1_dealer}, {answer2_dealer}, {answer3_dealer}]")
            print(f"Your final score: {user_score2}")
            print(f"The Dealer's final score: {answer1_dealer + answer2_dealer + answer3_dealer}")
            exit()

    elif question2 == "n":

        dealer_score2 = dealer_score1 + answer2_dealer + answer3_dealer

        print(f"Your final cards: [{answer1_user}, {answer2_user}]")
        print(f"Dealer's final cards: [{answer1_dealer}, {answer2_dealer}, {answer3_dealer}]")
        print(f"Your score final: {user_score1}")
        print(f"The Dealer's final score: {dealer_score2}")

        if dealer_score2 < user_score1:
            print("You Win")
            exit()
        elif dealer_score2 and user_score1 > 21:
            print("You both Lose")
            exit()
        elif dealer_score2 < 17 and user_score1 < 17:
            print("You both Lose")
            exit()
        elif dealer_score2 > 21 and user_score1 > 21:
            print("You both Lose")
            exit()
        elif dealer_score2 < 17 and user_score1 > 21:
            print("You both Lose")
            exit()
        elif dealer_score2 > 21 and user_score1 < 17:
            print("You both Lose")
        elif user_score1 < 17:
            print("You Lose")
            exit()
        elif dealer_score2 > 21:
            print("You Win")
            exit()
        elif dealer_score2 == user_score1:
            print("It's a Draw")
            exit()
        else:
            print("You Lose")
            exit()
    else:
        print("Invalid input")
        exit()

    c = " "
    print(c)

    question3 = input("Do you want another card? Y or N? ").lower()

    if question3 == "y":

        answer4_user = random.choice(cards)
        answer3_dealer = random.choice(cards3)

        user_score3 = user_score2 + answer4_user
        dealer_score1 = dealer_score + answer1_dealer

        print(f"Your cards: [{answer1_user}, {answer2_user}, {answer3_user}, {answer4_user}]")
        print(f"Dealer's first card: [{answer1_dealer}]")
        print(f"Your score is {user_score3}")
        print(f"The Dealer's score is {dealer_score1}")

        if user_score3 > 21:
            print(c)
            print("You Lose")
            print(f"Your final cards: [{answer1_user}, {answer2_user}, {answer3_user}, {answer4_user}]")
            print(f"Dealer's final cards: [{answer1_dealer}, {answer2_dealer}, {answer3_dealer}]")
            print(f"Your final score: {user_score3}")
            print(f"The Dealer's final score: {answer1_dealer + answer2_dealer + answer3_dealer}")
            exit()

    elif question3 == "n":

        dealer_score2 = dealer_score1 + answer2_dealer + answer3_dealer

        print(f"Your final cards: [{answer1_user}, {answer2_user}, {answer3_user}]")
        print(f"Dealer's final cards: [{answer1_dealer}, {answer2_dealer}, {answer3_dealer}]")
        print(f"Your final score: {user_score2}")
        print(f"The Dealer's final score: {dealer_score2}")

        if dealer_score2 < user_score2:
            print("You Win")
            exit()
        elif dealer_score2 and user_score2 > 21:
            print("You both Lose")
            exit()
        elif dealer_score2 < 17 and user_score2 < 17:
            print("You both Lose")
            exit()
        elif dealer_score2 > 21 and user_score2 > 21:
            print("You both Lose")
            exit()
        elif dealer_score2 < 17 and user_score2 > 21:
            print("You both Lose")
            exit()
        elif dealer_score2 > 21 and user_score2 < 17:
            print("You both Lose")
        elif user_score2 < 17:
            print("You Lose")
            exit()
        elif dealer_score2 > 21:
            print("You Win")
            exit()
        elif dealer_score2 == user_score2:
            print("It's a Draw")
            exit()
        else:
            print("You Lose")
            exit()
    else:
        print("Invalid input")
        exit()

    v = " "
    print(v)

    question4 = input("Do you want another card? Y or N? ").lower()

    if question4 == "y":

        answer5_user = random.choice(cards)

        user_score4 = user_score3 + answer5_user
        dealer_score1 = dealer_score + answer1_dealer

        print(f"Your cards: [{answer1_user}, {answer2_user}, {answer3_user}, {answer4_user}, {answer5_user}]")
        print(f"Dealer's first card: [{answer1_dealer}]")
        print(f"Your score: {user_score4}")
        print(f"The Dealer's score: {dealer_score1}")
        exit()

        if user_score4 > 21:
            print(v)
            print("You Lose")
            print(f"Your final cards: [{answer1_user}, {answer2_user}, {answer3_user}, {answer4_user}, {answer5_user}]")
            print(f"Dealer's final cards: [{answer1_dealer}, {answer2_dealer}, {answer3_dealer}]")
            print(f"Your final score: {user_score4}")
            print(f"The Dealer's final score: {answer1_dealer + answer2_dealer + answer3_dealer}")
            exit()

    elif question4 == "n":

        dealer_score2 = dealer_score1 + answer2_dealer
        dealer_score3 = dealer_score2 + answer3_dealer
        user_score4 = user_score3 + answer4_user

        print(f"Your final cards: [{answer1_user}, {answer2_user}, {answer3_user}, {answer4_user}]")
        print(f"Dealer's final cards: [{answer1_dealer}, {answer2_dealer}, {answer3_dealer}]")
        print(f"Your final score: {user_score3}")
        print(f"The Dealer's final score: {dealer_score3}")

        if dealer_score2 < user_score2:
            print("You Win")
            exit()
        elif dealer_score3 and user_score3 > 21:
            print("You both Lose")
            exit()
        elif dealer_score3 < 17 and user_score3 < 17:
            print("You both Lose")
            exit()
        elif dealer_score3 > 21 and user_score3 > 21:
            print("You both Lose")
            exit()
        elif dealer_score3 < 17 and user_score3 > 21:
            print("You both Lose")
            exit()
        elif dealer_score3 > 21 and user_score3 < 17:
            print("You both Lose")
        elif user_score3 < 17:
            print("You Lose")
            exit()
        elif dealer_score3 > 21:
            print("You Win")
            exit()
        elif dealer_score3 == user_score3:
            print("It's a Draw")
            exit()
        else:
            print("You Lose")
            exit()
    else:
        print("Invalid input")
        exit()

elif question == "n":
    exit()

else:
    print("Invalid input")
    exit()