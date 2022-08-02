from game_data import data
from random import choice
from art import vs
from art import logo
available_accounts = data
import os

account_a = choice(available_accounts)
available_accounts.remove(account_a)
account_b = choice(available_accounts)
available_accounts.remove(account_b)
option_list = [account_a, account_b]

def check_followers(winner, loser):
    if winner['follower_count'] > loser['follower_count']:
        return True
    else:
        return False

score = 0
is_user_correct = True

print(logo)
while is_user_correct and score <= 50:
    print(f"A: {account_a['name']} - The {account_a['description']}")
    print(f"From {account_a['country']}")
    print(vs)
    print(f"B: {account_b['name']} - The {account_b['description']}")
    print(f"From {account_b['country']}")
    user_choice = input("Who has more followers? 'A' or 'B'? ").lower()
    
    if user_choice == 'a':
        winner = account_a
        loser = account_b
    else:
        winner = account_b
        loser = account_a
    
    result = check_followers(winner, loser)
    
    if result == True:
        score += 1
        os.system('cls')
        print(logo)
        print("That's correct!")
        print(f"Your score: {score}")
        print("What do you think between these two: ")
        account_a = winner
        account_b = choice(available_accounts)
        available_accounts.remove(account_b)
        option_list = [account_a, account_b]
        
        if score == 50:
            print("You won!")
            break
    else:
        os.system('cls')
        print("Sorry! That's actually incorrect.")
        print(f"Your score: {score}")
        print("You can score much better that this!")
        is_user_correct = False
    
        
    

















    