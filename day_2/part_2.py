import re
from functools import reduce
from operator import mul

def extract_color_and_number(text):
    matches = re.findall(r'(\d+)\s+(\w+)', text)
    return [(int(amount), color) for amount, color in matches]


total_powers = 0

with open("input", "r") as file:
    for line in file:

        minimum = {
            "blue": -1,
            "green": -1,
            "red": -1
        }

        game = int(line.split(' ')[1].replace(':',''))
        rounds = line.split(':')[1]
        combinations = extract_color_and_number(rounds)

        for amount, color in combinations:
            if amount > minimum.get(color):
                minimum[color] = amount

        power = reduce(mul, minimum.values())
        total_powers += power

    print(total_powers)
