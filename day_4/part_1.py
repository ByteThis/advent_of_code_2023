value = 0
with open("input", "r") as file:
    for line in file:
        winning_numbers, my_numbers = line.split(':')[1].split('|')

        winning_numbers = [int(x) for x in winning_numbers.split()]
        my_numbers = [int(x) for x in my_numbers.split()]

        intersection = set(winning_numbers).intersection(set(my_numbers))

        if intersection:
            val = 2 ** (len(intersection)-1)
            value += val

print(value)
