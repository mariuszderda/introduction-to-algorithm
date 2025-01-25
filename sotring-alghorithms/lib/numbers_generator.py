import random

def random_list(number_of_items):
    random_numbers = []
    while len(random_numbers) < number_of_items:
        num = random.randint(1, number_of_items * 5)
        if num not in random_numbers:
            random_numbers.append(num)
    return random_numbers

def descending_list(number_of_items):
    return list(range(number_of_items - 1 , -1, -1))
