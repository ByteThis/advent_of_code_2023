import regex

total = 0

def convert_to_int_str(number):
    if number.isdigit():
        return number
    else:
        text_to_digit = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }
        return text_to_digit.get(number.lower(), number)

with open("input", "r") as file:
    for line in file:
        numbers = [convert_to_int_str(match[0] or match[1]) for match in
                   regex.findall(r'(?:(one|two|three|four|five|six|seven|eight|nine)|([1-9]))', line, overlapped=True)]

        total += int(numbers[0] + numbers[-1])

print(total)


