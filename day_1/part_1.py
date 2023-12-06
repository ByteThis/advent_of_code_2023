total = 0

with open("input", "r") as file:
    for line in file:
        x = [i for i in line if i.isdigit()]
        total += int(x[0]+x[-1])

print(total)
