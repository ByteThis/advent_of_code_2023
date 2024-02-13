from functools import reduce

def distance_traveled(time, speed):
    return speed * (time - speed)

file = open("input_test").read().strip().split("\n")
times = [int(x) for x in file[0].split(":")[1].strip().split(" ") if x]
distances = [int(x) for x in file[1].split(":")[1].strip().split(" ") if x]

winning_combos = []

for t, d in zip(times, distances):
    first_win = last_win = 0

    for i in range(1, t):
        if distance_traveled(t, i) > d:
            first_win = i
            break

    for i in range(t-1, 0, -1):
        if distance_traveled(t, i) > d:
            last_win = i
            break

    print(first_win, last_win)
    winning_combos.append(last_win-first_win+1)

out = reduce(lambda x, y: x*y, winning_combos)
print(out)