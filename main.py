from random import choice
from game_data import data

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f'{name}, {description}, from {country}.'

def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        answer = 'a'
    else:
        answer = 'b'
    return guess == answer

print('\nWelcome to the * Higher - Lower * game.\n')

should_continue = True
score = 0
while should_continue:
    account_a = choice(data)
    account_b = choice(data)

    print(format_data(account_a))
    print(' VS. ')
    print(format_data(account_b))

    user_guess = input('\nWho have more followers?: Type "A" or "B": ').lower()

    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']

    correct_answer = check_answer(user_guess, followers_a, followers_b)

    if correct_answer:
        score +=1
    else:
        should_continue = False
print(f'Final score: {score}.')