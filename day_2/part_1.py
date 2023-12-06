import re

def extract_color_and_number(text):
    matches = re.findall(r'(\d+)\s+(\w+)', text)
    return [(int(amount), color) for amount, color in matches]

limits = {
    "blue": 14,
    "green": 13,
    "red": 12
}

valid_games = []

with open("input", "r") as file:
    for line in file:
        valid = True
        game = int(line.split(' ')[1].replace(':',''))
        rounds = line.split(':')[1]
        combinations = extract_color_and_number(rounds)
        for amount, color in combinations:
            if limits.get(color) < amount:
                valid = False
                break

        if valid:
            valid_games.append(game)

    print(sum(valid_games))
