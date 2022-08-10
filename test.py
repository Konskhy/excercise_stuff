import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]
# create dictionary with name : len(mathing_numbers) pairs using dict comprehension
winnings = {i['name']: len(i['numbers'].intersection(lottery_numbers)) for i in players}
# check records for max value
numbers_matched = max(winnings.values())
# retrieve the key of max value
winner_name = max(winnings, key=winnings.get)

print(f'{winner_name} won {100 ** numbers_matched}.')



