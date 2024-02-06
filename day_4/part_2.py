from collections import defaultdict

total_scratch_cards = 0
repeat_cards = defaultdict(int)

with open("input", "r") as file:
    for i, line in enumerate(file):
        total_scratch_cards += repeat_cards[i]+1

        winning_numbers, my_numbers = line.split(':')[1].split('|')

        winning_numbers = [int(x) for x in winning_numbers.split()]
        my_numbers = [int(x) for x in my_numbers.split()]

        intersection = set(winning_numbers).intersection(set(my_numbers))
        matching_numbers = len(intersection)

        for x in range(matching_numbers):
            repeat_cards[i+x+1] += repeat_cards[i]+1

print(total_scratch_cards)
