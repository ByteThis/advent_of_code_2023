import re


def extract_number_groups_with_indices(input_string):
    number_groups = re.finditer(r'\d+|d', input_string)
    extracted_data = [(int(match.group()), match.start()) for match in number_groups]
    return extracted_data


def get_indices_for_numbers(single_digit_group):
    number, start_index = single_digit_group
    if start_index > 0:
        start_index -= 1
    return list(range(start_index, start_index + len(str(number)) + 2))


input_string = "abc*def#ghi$"
special_chars = "*#$+@/%-&="

previous_special_char_indexes = []
previous_valid_numbers = []

parts = []


def handle_line(line):
    for c in special_chars:
        line = line.replace(c, '')
    return line


with open("input", "r") as file:
    for line in file:

        print(line)

        numbers = extract_number_groups_with_indices(line)
        special_char_indexes = [i for i, char in enumerate(line) if char in special_chars]

        # handle same line matching
        if special_char_indexes and numbers:
            print("same line!!")
            for n in numbers:
                if set(special_char_indexes).intersection(set(get_indices_for_numbers(n))):
                    parts.append(n[0])
                    print(f"validated {n[0]}")

        # validate previous line
        if special_char_indexes and previous_valid_numbers:
            print("got old digits to validate with these symbols")
            for n in previous_valid_numbers:
                if set(special_char_indexes).intersection(set(get_indices_for_numbers(n))):
                    parts.append(n[0])
                    print(f"validated {n[0]}")

        # validate this line with previous symbols
        if numbers and previous_special_char_indexes:
            print("got old symbols to validate digits")
            print(numbers)
            print(previous_special_char_indexes)

            for n in numbers:
                print(get_indices_for_numbers(n))
                if set(previous_special_char_indexes).intersection(set(get_indices_for_numbers(n))):
                    parts.append(n[0])
                    print(f"validated {n[0]}")

        previous_valid_numbers = numbers
        previous_special_char_indexes = special_char_indexes

        print("\n\n")

    print(parts)
    print(sum(parts))