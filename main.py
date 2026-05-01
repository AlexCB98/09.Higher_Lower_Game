from random import choice
from game_data import data

print('\nWelcome to the * Higher - Lower * game.\n')

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f'{name}, {description}, from {country}.'

account_a = choice(data)
account_b = choice(data)

user_guess = input('Who have more followers?: Type "A" or "B": ').lower()

def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        answer = 'a'
    else:
        answer = 'b'
    return guess == answer