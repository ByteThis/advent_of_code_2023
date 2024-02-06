import re
from collections import defaultdict
from functools import reduce

def extract_number_groups_with_indices(input_string):
    number_groups = re.finditer(r'\d+|d', input_string)
    extracted_data = [(int(match.group()), match.start()) for match in number_groups]
    return extracted_data


def get_indices_for_numbers(single_digit_group):
    number, start_index = single_digit_group
    if start_index > 0:
        start_index -= 1
    return list(range(start_index, start_index + len(str(number))+2))


special_chars = "*"

previous_special_char_indexes = []
previous_valid_numbers = []

parts = []

gear_values = defaultdict(list)

with open("input", "r") as file:
    for l, line in enumerate(file):
        numbers = extract_number_groups_with_indices(line)
        special_char_indexes = [i for i, char in enumerate(line) if char in special_chars]

        # handle same line matching
        if special_char_indexes and numbers:
            for n in numbers:
                if set(special_char_indexes).intersection(set(get_indices_for_numbers(n))):
                    for x in set(special_char_indexes).intersection(set(get_indices_for_numbers(n))):
                        gear_values[f"{l},{x}"].append(n[0])
                    parts.append(n[0])

        # validate previous line
        if special_char_indexes and previous_valid_numbers:
            for n in previous_valid_numbers:
                if set(special_char_indexes).intersection(set(get_indices_for_numbers(n))):
                    for x in set(special_char_indexes).intersection(set(get_indices_for_numbers(n))):
                        gear_values[f"{l},{x}"].append(n[0])
                    parts.append(n[0])

        # validate this line with previous symbols
        if numbers and previous_special_char_indexes:
            for n in numbers:
                if set(previous_special_char_indexes).intersection(set(get_indices_for_numbers(n))):
                    for x in set(previous_special_char_indexes).intersection(set(get_indices_for_numbers(n))):
                        gear_values[f"{l-1},{x}"].append(n[0])
                    parts.append(n[0])

        previous_valid_numbers = numbers
        previous_special_char_indexes = special_char_indexes

    gears = []
    for k,v in gear_values.items():
        if len(v) == 2:
            gears.append(reduce((lambda x, y: x * y), v))

    print(sum(gears))
