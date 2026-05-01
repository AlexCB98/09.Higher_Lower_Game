from random import choice
from game_data import data
from art import vs, logo

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f'{name}, a {description}, from {country}.'

def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        answer = 'a'
    else:
        answer = 'b'
    return guess == answer

print(logo)
print('Welcome to the * Higher - Lower * game.\n')

should_continue = True
score = 0
account_b = choice(data)

while should_continue:
    print('Choose from:')

    account_a = account_b
    account_b = choice(data)

    while account_b == account_a:
        account_b = choice(data)

    print(format_data(account_a))
    print(vs)
    print(format_data(account_b))

    user_guess = input('\nWho has more followers?: Type "A" or "B": ').lower()

    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']

    correct_answer = check_answer(user_guess, followers_a, followers_b)

    if correct_answer:
        score +=1
        print('\n' * 20)
        print(logo)
        print(f'*** Your score is: {score}')
    else:
        should_continue = False

print(f'Wrong. Final score: {score}.')