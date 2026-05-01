from random import choice
from game_data import data

print('\nWelcome to the * Higher - Lower * game.\n')

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f'{name}, {description}, from {country}.'

print(format_data(data[0]))
